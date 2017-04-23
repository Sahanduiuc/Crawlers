# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class GuruItem(scrapy.Item):
    symbol=scrapy.Field()
    #scorecard=scrapy.Field()
    p_slash_e=scrapy.Field()
    value = scrapy.Field()
    momentum_strategy = scrapy.Field()
    growth_slash_value1=scrapy.Field()
    small_cap_growth=scrapy.Field()
    contrarian = scrapy.Field()
    growth_slash_value2=scrapy.Field()
    price_slash_sales=scrapy.Field()


class NsdqItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
