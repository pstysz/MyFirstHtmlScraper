# -*- coding: utf-8 -*-
import logging
import django
import time
from functions import *

#region Configuration

#TODO: Add logging to file
#eg: logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
root_url = 'http://www.wykop.pl/wykopalisko/'
site_pattern = root_url + 'strona/{{site_number}}/' #{{site_number}} is taken from last site number
django.setup()

#endregion Configuration

#region Initialization

base_soup = get_soup_for_url(root_url)

no_of_sites = get_last_site_number(base_soup)

#endregion Initialization

logging.info('Found {0} sites to scrap'.format(no_of_sites))
start_time = time.time()
scrap_sites(no_of_sites, site_pattern)
logging.info('Scraping took {0}'.format(time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))))