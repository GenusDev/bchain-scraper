
# from urllib2 import urlopen
# from urllib.request import urlopen, request
# import urllib.request
# from bs4 import BeautifulSoup

# ***************
# query the website and get the html page, set to  variable ‘page’
# ******** THESE BACK TICKS FUCK EVERYTHING UP: ‘page’ **********


# page = urllib2.urlopen(angel_page_blockchain_nyc)

# parse the html using beautiful soup and store in variable `soup`
# soup = BeautifulSoup(page, 'html.parser')


# Now we have a variable, soup, containing the HTML of the page.
# Here’s where we can start coding the part that extracts the data.

# BeautifulSoup can help us get into these page layers and extract the content with find().
# In this case, since the HTML class 'name' is unique on this page,
# we can simply query <div class="name">.

# div class="header-info" gives the company name, bio, current positions,
# "active this week", and # of employees

# inside that is div class="startup-link" which is their company name
# inside that is div class="browse-table-row-name"
# inside header0info is class="tagline" ==> company bio
        # limity this to 25 chars for spreadsheet


# take out the <div> of an a tag and get its value
# name_box = soup.find('a', attrs={'class': 'startup-link'})

# now get at its text
# strip() is used to remove starting and trailing
# name = name_box.text.strip()
# print name



# information to consider:
# currently hiring?
# hiring more than 3 people
# still looking for CEO / CTO
# early stages?

# at the top
# -*- coding: utf-8 -*-
# ^ After error inserted this:
# If you are just trying to use UTF-8 characters or don't care if
# they are in your code, add this line to the top of your .py file
# https://stackoverflow.com/questions/21639275/python-syntaxerror-non-ascii-character-xe2-in-file
