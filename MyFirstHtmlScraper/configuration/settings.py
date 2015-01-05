# -*- coding: utf-8 -*-
import logging
import sys
import os
from peewee import *

'''DO NOT INCLUDE THIS FILE TO SOURCE CONTROL!!!'''

#region General Settings
APP_DIR = os.path.dirname(os.path.dirname(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
#endregion General Settings

#region Database Settings
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
DB_HANDLER = MySQLDatabase(**DBSETTINGS['mysql'])
#endregion Database Settings

#region Kicker Settings
KICKER_ROOT_URL = 'http://www.wykop.pl/wykopalisko/'
KICKER_SUBSITE_PATTERN = KICKER_ROOT_URL + 'strona/{{site_number}}/' #{{site_number}} is taken from last site number
#endregion Kicker Settings

#region PcLab Settings
PCLAB_SITE_PATTERN =  'http://pclab.pl/news-{{site_number}}-100.html' 
PCLAB_ARTICLE_PATTERN = 'http://pclab.pl/news{{article_id}}.html'
#endregion PcLab Settings

#region Content Settings
MAX_USAGE_CONT = 5  # how many times can single content be used to generate new article
#endregion Content Settings