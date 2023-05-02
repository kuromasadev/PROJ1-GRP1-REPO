import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import time
import csv
import numpy as np

# Load the archival site into a request and into the web scraper
url = "https://www.jt-sw.com/football/pro/teams.nsf/histories/eagles”
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Use Beautiful Soup to find all the anchor tags within the "pre" tag of the HTML content
pre_tag = soup.find('pre')
a_tags = pre_tag.find_all('a')

# Loop through the list of links and use requests to make a request to each link but only that start between 2015-2021
links_2015 = []
links_2016 = []
links_2017 = []
links_2018 = []
links_2019 = []
links_2020 = []
links_2021 = []


for a in a_tags:
    if a.has_attr('href') and a['href'].startswith(('2015')):
        links_2015.append(a['href'])
    if a.has_attr('href') and a['href'].startswith(('2016')):
       links_2016.append(a['href'])
    if a.has_attr('href') and a['href'].startswith(('2017')):
       links_2017.append(a['href'])
    if a.has_attr('href') and a['href'].startswith(('2018')):
       links_2018.append(a['href'])
    if a.has_attr('href') and a['href'].startswith(('2019')):
       links_2019.append(a['href'])
    if a.has_attr('href') and a['href'].startswith(('2020')):
       links_2020.append(a['href'])
    if a.has_attr('href') and a['href'].startswith(('2021')):
       links_2021.append(a['href'])

# Define the lists of links and the combo dataframe with all years
links = [links_2015, links_2016, links_2017, links_2018, links_2019, links_2020, links_2021]
week_allcharts_df = []

# Loop through each list of links
for link_list in tqdm(links, desc='Overall Year progress', position=0):
    # Loop through each link in the list

