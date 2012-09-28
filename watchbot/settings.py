# Scrapy settings for watchbot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'watchbot'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['watchbot.spiders']
NEWSPIDER_MODULE = 'watchbot.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

