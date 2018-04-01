# DOESNT WORK, DATA IS PROTECTED ON ANGEL

# import libraries
import urllib2
# import urllib.request  as urllib2
from bs4 import BeautifulSoup


# blockchain companies on Angel listed in NYC
angel_page_blockchain_nyc = "https://angel.co/new-york-ny-1/blockchains/jobs";

page = urllib2.urlopen(angel_page_blockchain_nyc)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

print soup

# Now we have a variable, soup, containing the HTML of the page.
# Heres where we can start coding the part that extracts the data.

# BeautifulSoup can help us get into these page layers and extract the content with find().
# In this case, since the HTML class name is unique on this page,
# we can simply query <div class="name">.

# div class="header-info" gives the company name, bio, current positions,
# "active this week", and # of employees

# inside that is div class="startup-link" which is their company name
# inside that is div class="browse-table-row-name"
# inside header0info is class="tagline" ==> company bio
        # limity this to 25 chars for spreadsheet

# take out the <div> of an a tag and get its value
# name_box = soup.find('a', attrs={'class': 'startup-link'})
name_box = soup.find('div', attrs={'class': 'browse-table-row-name'})
print name_box
# now get at its text
# strip() is used to remove starting and trailing
# name = name_box.text.strip()
# print name
