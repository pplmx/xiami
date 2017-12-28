# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiamiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 网页的标题
    title = scrapy.Field()
    # 用户的名字
    name = scrapy.Field()
    # 歌单的歌名
    song = scrapy.Field()
    pass
