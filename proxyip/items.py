# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyipItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
    address = scrapy.Field()
    type_id = scrapy.Field()
    speed = scrapy.Field()
    proving_time = scrapy.Field()

