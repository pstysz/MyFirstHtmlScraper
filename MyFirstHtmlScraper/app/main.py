import requests
import bs4
import time
import logging
from functions import get_soup_for_url, get_last_site_number, get_links

#region Configuration

#TODO: Add logging to file
#eg: logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
root_url = 'http://www.wykop.pl/'
site_pattern = root_url + 'strona/{{site_number}}/' #{{site_number}} is taken from last site number

#endregion Configuration

#region Initialization

base_soup = get_soup_for_url(root_url)

no_of_sites = 1 #get_last_site_number(base_soup)

#endregion Initialization


for site_number in range(1, no_of_sites + 1):
    url = site_pattern.replace('{{site_number}}', str(site_number))
    soup = get_soup_for_url(url)
    links_to_track = get_links(soup)
    print(links_to_track)