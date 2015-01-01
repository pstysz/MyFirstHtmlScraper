# -*- coding: utf-8 -*-
import requests
import logging
import bs4
import multiprocessing
import re
import sys
import os
sys.path.append('../orm/')
sys.path.append('.')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm.settings")
from app.models import Post, Category
from dateutil.parser import parse
from global_functions import get_urls_from_pattern
