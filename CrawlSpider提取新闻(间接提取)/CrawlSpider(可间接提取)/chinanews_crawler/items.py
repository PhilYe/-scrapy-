# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class NewsFeedItem(Item):
    title = Field()
    link = Field()
    desc = Field()
    pub_date = Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
