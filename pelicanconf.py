#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'CompLab'
SITENAME = u'Computational Linguistics Lab'
# SITESUBTITLE = u'Computational Linguistics at Stony Brook University'
SITEURL = 'http://localhost:8000/output'
GITHUB_URL = 'https://github.com/CompLab-StonyBrook/website'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
FEED_MAX_ITEMS = 8

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

LOAD_CONTENT_CACHE = False
TYPOGRIFY = True

# Set up basic plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['extract_toc']

MARKDOWN = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.headerid': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

# Theme
THEME = 'themes/sbu'

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

# should title and details be shown on index.html?
LANDING_PAGE_ABOUT = (
{'title': True,
 'details': True})

# sidebar of projects; co-opted for contact info
PROJECTS = [{
    'name': 'Lab Director',
    'url': 'jeffrey.heinz@stonybrook.edu',
    'description': 'Jeffrey Heinz'},
    {'name': 'M.A. Program Director',
     'url': 'maprogram@thomasgraf.net',
     'description': 'Thomas Graf'},
    {'name': 'Website Administrator',
     'url': 'website@thomasgraf.net',
     'description': 'Thomas Graf'}
    ]


# SLUGIFY_SOURCE = 'basename'
# ARTICLE_SAVE_AS = '{slug}.html'

# Custom Menu
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
PAGE_ORDER_BY = 'page-order'

# MENUITEMS = (
#     ('Programs', '/pages/programs.html'),
#     ('People', '/pages/people.html'),
#     ('Alumni', '/pages/alumni.html'),
#     ('Research', '/pages/research.html'),
#     ('Resources', '/pages/software-resources.html'),
# )

# Tricks to deal with special files
STATIC_PATHS = ['theme/images', 'images', 'doc', 'extra/CNAME', 'extra/README.md']
STATIC_EXCLUDE_SOURCES = False
IGNORE_FILES = ['extra']
EXTRA_PATH_METADATA = {
    'extra/README.md': {'path': 'README.md'},
    'extra/CNAME': {'path': 'CNAME'}
}

# We have our start page, so the index needs a different name
# INDEX_SAVE_AS = 'news.html'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['README.md', '.git', '.gitignore']

# this is needed to get an index.html
DEFAULT_DATE = 'fs'

# no author page
AUTHOR_SAVE_AS = ''
# no tag page
TAG_SAVE_AS = ''
# no category page
CATEGORY_SAVE_AS = ''
