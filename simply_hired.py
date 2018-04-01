# import urllib.request  as urllib2
import urllib2
from bs4 import BeautifulSoup

# csv
import csv
from datetime import datetime


simply_hired_blockchain_nyc = "https://www.simplyhired.com/search?q=blockchain+companies&l=new+york%2C+ny&job=pbcpy1ka232JyFd5QmKtVebiGY0EhcwOuLJBiwOuJDYXBU5cCEzc6A"

page = urllib2.urlopen(simply_hired_blockchain_nyc)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')
# companies = {}
names_locations_raw = soup.find_all('h3', attrs={'class': 'jobposting-subtitle'})
companies = list(map(lambda x: x.text.strip().encode('ascii', 'ignore').split(" - ")[0], names_locations_raw))
# my_list = list(enumerate(lambda x: companies[x.text.strip().encode('ascii', 'ignore').split("-")[0]] = x.text.strip().encode('ascii', 'ignore').split("-")[1], names_locations_raw))
# cities = list(map(lambda x: x.text.strip().encode('ascii', 'ignore').split(" - ")[1], names_locations_raw))


print companies
# print cities

# to open a csv file with APPEND, so that old data will not be erased use:
# with open('index.csv', 'a') as csv_file:
# this will re-write companies data to index.csv
with open('simply_hired_index.csv', 'w') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([companies])




# companies = {}
#
# for i in range(5):
#     simply_hired_blockchain_nyc = "https://www.simplyhired.com/search?q=blockchain+companies&l=new+york%2C+ny&job=pbcpy1ka232JyFd5QmKtVebiGY0EhcwOuLJBiwOuJDYXBU5cCEzc6A"
#     page = urllib2.urlopen(simply_hired_blockchain_nyc)
#     # parse the html using beautiful soup and store in variable `soup`
#     soup = BeautifulSoup(page, 'html.parser')
#     sub_title = soup.find('h3', attrs={'class': 'jobposting-subtitle'})
#     sub_title = sub_title.text.strip()
#     name = sub_title.split("-")[0]
#     location = sub_title.split("-")[1]
#     print i
#     if name not in companies:
#         companies[name] = location
#
# print companies
