# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 名字
    name = scrapy.Field()
    #
    des = scrapy.Field()

    link = scrapy.Field()
    info = scrapy.Field()
    follow = scrapy.Field()
    total = scrapy.Field()
    price = scrapy.Field()

    name_id = scrapy.Field()

    image = scrapy.Field()
    pass
