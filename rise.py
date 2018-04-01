# import urllib.request  as urllib2
import urllib2
from bs4 import BeautifulSoup

# csv
import csv
from datetime import datetime

rise_top_100_blockchain = "https://www.rise.global/blockchain-100";


page = urllib2.urlopen(rise_top_100_blockchain)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# print soup

names_raw = soup.find_all('a', attrs={'class': 'player-username'})
bios_raw = soup.find_all('p', attrs={'class': 'player-bio'})
# name = soup.find('a', attrs={'class': 'player-username'})
# bio = soup.find('p', attrs={'class': 'player-bio'})

names = list(map(lambda x: x.text.strip().encode('ascii', 'ignore'), names_raw))
bios = list(map(lambda x: x.text.strip().encode('ascii', 'ignore').translate(None, ','), bios_raw))
bios_truncated = list(map(lambda x: x.text.strip().encode('ascii', 'ignore')[:44].translate(None, ','), bios_raw))

# print bios

with open('rise_names_index.csv', 'w') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([names])


with open('rise_bios_index.csv', 'w') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([bios])

with open('rise_bios_trunc.csv', 'w') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([bios_truncated])
