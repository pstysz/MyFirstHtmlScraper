# -*- coding: utf-8 -*-
import logging
import os
import sys
import django
sys.path.append('../orm/')
sys.path.append('.')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm.settings")
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

no_of_sites = 1 # get_last_site_number(base_soup)

#endregion Initialization

scrap_sites(no_of_sites, site_pattern)