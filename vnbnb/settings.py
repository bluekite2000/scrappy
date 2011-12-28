# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'vnbnb'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['vnbnb.spiders']
NEWSPIDER_MODULE = 'vnbnb.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline']
IMAGES_STORE = '/Users/trang/Desktop/scrapy/vnbnb/hanoiimages'
