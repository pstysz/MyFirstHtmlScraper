# -*- coding: utf-8 -*-
import logging
import sys
import os
from peewee import *

'''DO NOT INCLUDE THIS FILE TO SOURCE CONTROL!!!'''

APP_DIR = os.path.dirname(os.path.dirname(__file__))

#sys.path.append(os.path.join(APP_DIR, 'common'))
#sys.path.append(os.path.join(APP_DIR, 'configuration'))
#sys.path.append(os.path.join(APP_DIR, 'models'))
#sys.path.append(os.path.join(APP_DIR, 'scrapers'))
#sys.path.append(os.path.join(APP_DIR, 'tests'))

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

DBSETTINGS = {
    'mysql': {
        'database': 'content_generators',
        'user': 'pstysz',
        'passwd': 'pspsps',
        'host': 'localhost',
        'port': 3306
    },
    'sqlite3':{
        'database': 'test.db'
    }
}

KICKER_ROOT_URL = 'http://www.wykop.pl/wykopalisko/'
KICKER_SUBSITE_PATTERN = KICKER_ROOT_URL + 'strona/{{site_number}}/' #{{site_number}} is taken from last site number

PCLAB_SITE_PATTERN =  'http://pclab.pl/news-{{site_number}}-100.html' 
PCLAB_ARTICLE_PATTERN = 'http://pclab.pl/news{{article_id}}.html'

DB_HANDLER = MySQLDatabase(**DBSETTINGS['mysql'])