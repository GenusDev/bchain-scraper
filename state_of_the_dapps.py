# import libraries
import urllib2
# import urllib.request  as urllib2
from bs4 import BeautifulSoup


# blockchain companies on Angel listed in NYC
dapp_list = "https://www.stateofthedapps.com/tagged/finance/tab/most-relevant";


page = urllib2.urlopen(dapp_list)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# print soup

# dapp = soup.find_all('section')

# print dapp

dapp_companies_raw = soup.find_all('section', attrs={'class': 'section -items'})
print dapp_companies_raw
# dapp_companies_list = list(map(lambda x: x.text.strip().encode('ascii', 'ignore'), dapp_companies_raw))


# print dapp_companies_list
