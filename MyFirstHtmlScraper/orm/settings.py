# -*- coding: utf-8 -*-
from django.conf import settings
import os
import app
from django.db import models
from app import *

try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass 

APP_DIR  = os.path.dirname(app.__file__)
DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.mysql',
        # Or path to database file if using sqlite3.
        'NAME': 'content_generators',
        # Not used with sqlite3.
        'USER': 'pstysz',
        # Not used with sqlite3.
        'PASSWORD': '23PaweL74',
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '',
        # Set to empty string for default. Not used with sqlite3.
        'PORT': '3306',
    }
}
SECRET_KEY = 'n(bd1f1c%e8=_xad02x5qtfn%wgwpi492e$8_erx+d)!tpeoim'
INSTALLED_APPS  = ("app",)
MIDDLEWARE_CLASSES = ('',) #required to disable warning
