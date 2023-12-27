# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HuashiproItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    title = scrapy.Field()
    likeNum = scrapy.Field()
    src = scrapy.Field()
    page = scrapy.Field()
    pass
