#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Josh Wickham'
SITENAME = u'i-Josh'
SITEURL = 'http://localhost:8000'

HEADER_IMG_URL = SITEURL + '/images/home_profile_img_1.png'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = 'silk-pajamas'

PLUGIN_PATHS =['plugins']
PLUGINS = ['panoviewer.panoviewer', 'summary.summary', 'cachebuster.cachebuster', 'post.post', 'fb_meta']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/XerxesDGreat'),
    ('facebook', 'https://facebook.com/josh.wickham'),
    ('github', 'https://github.com/XerxesDGreat'),
    ('steam-square', 'https://steamcommunity.com/id/xerxesdgreat/games/')
)

SUMMARY_MAX_LENGTH = 100

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Where to look for static content
STATIC_PATHS = ['panorama', 'images']

# extensions to be used by Markdown
MD_EXTENSIONS = ['attr_list', 'codehilite']

###############################################################################
# TEMPLATE OPTIONS

# About blurb; shows up on home page
ABOUT_PERSONAL_INFO = 'I\'m a software engineer who has several joys in life: a great wife, a wonderful daughter, a good job ' \
                'at an exciting startup in San Francisco, and enough skill and means to have woodworking, knitting, ' \
                'cooking, LEGO, music, and -- of course -- writing my own software applications. One thing I share across ' \
                'all of these subjects is a drive to excel at the project, to hone my existing skill, to learn something ' \
                'new, essentially, to craft something I can feel proud of.'

# Photo for About section, shows up on home page
ABOUT_PERSONAL_PHOTO = 'home_profile_img_1.jpg'

# List of tuples with work information; used on home page and in side bar
# Valid work_types are:
# - 'image': when clicked, will generate a lightbox with the image identified by work_link
# - 'video': when clicked, will generate a lightbox with the video identified by work_link embedded. Tested with YouTube and Vimeo
# - 'link': when clicked, will open up the url identified by work_link
# WORK_LIST = [
#     #(work_type, work_preview_img_url, work_title, work_description, work_link)
#     ('image', 'http://localhost:8000/images/dsc_2609.jpg', 'A Scarf for Cora', 'I made this scarf for cora, using Moss stitch', 'http://localhost:8000/images/dsc_2609.jpg'),
#     ('video', 'http://localhost:8000/images/dsc_2607.jpg', 'Sample Video 1', 'This is a sample YouTube video', 'http://www.youtube.com/watch?v=kh29_SERH0Y?rel=0'),
#     ('video', 'http://localhost:8000/images/bugzilla.jpg', 'Sample Video 2', 'This is a sample Vimeo video', 'http://vimeo.com/23630702'),
#     ('link', 'http://localhost:8000/images/board_selection.jpg', 'Sample link 1', 'Let\'s see what happens with a sample link', 'http://www.i-josh.com'),
#     ('link', 'http://localhost:8000/images/calendar_view.jpg', 'Sample link 2', 'I think it should be pretty cool', 'http://www.google.com')
# ]

MAIN_IMAGES = [
    'dsc_2287.jpg',
    '2014_09_20_04_11_27.jpg',
    '2014_09_23_04_16_36.jpg',
    '2014_09_27_09_02_02.jpg',
    '2014_09_23_04_17_37.jpg',
    '2014_09_21_05_51_48.jpg',
    '2014_09_20_10_42_34.jpg',
    '2014_09_24_09_07_24.jpg'
]

SHARE_POST_LINKS = False

###############################################################################
# FACEBOOK SHARING OPTIONS
FACEBOOK_APP_ID = '155022494569896'
FACEBOOK_OPENGRAPH_TAGS = True
FACEBOOK_ENABLE_SHARING = True
FACEBOOK_ENABLE_COMMENTS = True
FACEBOOK_ENABLED = FACEBOOK_OPENGRAPH_TAGS or FACEBOOK_ENABLE_COMMENTS or FACEBOOK_ENABLE_COMMENTS
