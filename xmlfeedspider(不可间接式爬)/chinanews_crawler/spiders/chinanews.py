# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from ..items import NewsFeedItem


class ChinaNewsXmlFeedSpider(XMLFeedSpider):
    name = 'chinanews'
    start_urls = ('http://www.chinanews.com/rss/scroll-news.xml',)

    def parse_node(self, response, node):
        item = NewsFeedItem()
        item['title'] = node.xpath('title/text()').get()##这里不用extract_first(),新版本用get()更好
        item['link'] = node.xpath('link/text()').get()
        item['desc'] = node.xpath('description/text()').get()
        item['pub_date'] = node.xpath('pubDate/text()').get()

        yield item
