# Kworb Dataset Extraction 

Metadata

About Dataset

Context 

Content

# Extraction Script 

```python
#Dependencies 

import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import time
import csv
import numpy as np

# Load the archival site into a request and into the web scraper
url = "https://kworb.net/ww/archive/"
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
    for link in tqdm(link_list, desc=f'Links in {link_list[0][:4]}', position=1, leave=False):
        try:
        # Step 1: Use Beautiful Soup to parse the HTML content of each link and find the table tag within the HTML content.
            link_final = requests.get(url+link)
            link_soup_final = BeautifulSoup(link_final.content, 'html.parser')
          # Step 2: Find the table in the html code
            table_final = link_soup_final.find('table')
        # Step 3: Use pandas library to read the html table into dataframe
            weekchart_df = pd.read_html(str(table_final))[0].iloc[:,:9]
        # Step 4: Extract the date code from the url link as use it as a week label for future sorting
            weeklabel = link[:8]
            weekchart_df ['Week'] = weeklabel
        # Step 5: Append the dataframe to the list of dataframes
            week_allcharts_df.append(weekchart_df)
        except:
            print(f'Error processing link: {link}')

### progress bar is going to look like 
### Overall Year progress: 100%|██████████| 7/7 [1:13:38<00:00, 631.27s/it]

# Concatenate all dataframes in week_allcharts_df list into a single dataframe
week_allcharts_df = pd.concat(week_allcharts_df, ignore_index=True)

# <class 'pandas.core.frame.DataFrame'> RangeIndex: 565600 entries, 0 to 565599 Data columns (total 13 columns): 
# dtypes: float64(3), int64(3), object(7) 
# memory usage: 56.1+ MB

# export the dataframe to a CSV file with high efficiency
chunk_size = 10000 # adjust this to a size that works for your system
df_list = [chunk for _, chunk in week_allcharts_df.groupby(np.arange(len(week_allcharts_df)) // chunk_size)]
with open('../test chamber/week_allcharts_df_v01.csv', 'w') as f:
    writer = csv.writer(f)
    pbar = tqdm(total=len(week_allcharts_df))
    for chunk in df_list:
        chunk.to_csv(f, index=False, header=False)
        pbar.update(len(chunk))
    pbar.close()

# RESULT SHOULD BE A COMBINED CSV THAT CAN BE READ INTO FOR ANALYSIS
# Processing Time clocks arund 73 minutes and 39 seconds
```

