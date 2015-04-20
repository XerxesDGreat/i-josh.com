#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.i-josh.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-59670577-1"

PERSONAL_PHOTO = 'http://www.i-josh.com/images/10336807101524288927696705237706410271543060n.jpg'

HEADER_IMG_URL = SITEURL + '/images/home_profile_img_1.png'