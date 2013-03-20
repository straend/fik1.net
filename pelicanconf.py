#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Tomas Strand'
SITENAME = u'fik1'
SITEURL = 'http://fik1.net'
AUTHOR_EMAIL = u'tomas@fik1.net'
AUTHOR_PHONE = u'+358 50 5649 847'
TIMEZONE = 'Europe/Helsinki'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

THEME = 'themes/pelican-purple'
STATIC_PATHS = ["images", ]

MARKUP = 'md'



GITHUB_URL = 'http://github.com/straend/'
GOOGLE_ANALYTICS = 'UA-6766930-16'
DISQUS_SITENAME = 'fik1'

PLUGINS = ['pelican.plugins.latex',]

# Should we show a vCard of the author, its only visible in the source
VCARD = True
AUTHOR_ADDRESS = (
	('street-address', 	u'Simsalö'),
	('postal-code', 	u'01120'),
	('locality', 		u'Västerskog'),
	('country-name', 	u'Finland'),
)


FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Social widget
SOCIAL = (
	('github', 		'https://github.com/straend/'),
	('linkedin', 	'http://fi.linkedin.com/in/strandt'),
	('facebook', 	'https://facebook.com/strandt/'),
	('google-plus',	'https://plus.google.com/112133210939722958756/'),

)

ARTICLE_URL 		= '{date:%Y}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS 	= '{date:%Y}/{date:%d}/{slug}/index.html'

TAG_URL 			= 'tags/{slug}/'
TAG_SAVE_AS 		= 'tags/{slug}/index.html'

CATEGORY_URL 		= '{slug}/'
CATEGORY_SAVE_AS 	= '{slug}/index.html'

DEFAULT_PAGINATION = 5
