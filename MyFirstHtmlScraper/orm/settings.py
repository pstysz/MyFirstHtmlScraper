# -*- coding: utf-8 -*-
from django.conf import settings
import os
import app
from django.db import models
from app import *

APP_DIR  = os.path.dirname(app.__file__)
DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': os.path.join(APP_DIR, 'db.sqlite3'),
        # Not used with sqlite3.
        'USER': '',
        # Not used with sqlite3.
        'PASSWORD': '',
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '',
        # Set to empty string for default. Not used with sqlite3.
        'PORT': '',
    }
}
SECRET_KEY = 'n(bd1f1c%e8=_xad02x5qtfn%wgwpi492e$8_erx+d)!tpeoim'
INSTALLED_APPS  = ("app",)
MIDDLEWARE_CLASSES = ('',) #required to disable warning
