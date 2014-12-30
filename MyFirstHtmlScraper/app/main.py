# -*- coding: utf-8 -*-
import requests
import bs4
import time
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

scraped_posts = Post.objects.all()


for site_number in range(1, no_of_sites + 1):
    url = site_pattern.replace('{{site_number}}', str(site_number))
    soup = get_soup_for_url(url)
    create_posts_from_soup(soup)

    print(sys.stdout.encoding)