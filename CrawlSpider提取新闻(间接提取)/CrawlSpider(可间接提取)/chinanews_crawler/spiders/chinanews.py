# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule  ##注意这里的写法，已经更新了，直接scrapy.spiders。
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from ..items import NewsFeedItem


class ChinaNewsXmlFeedSpider(CrawlSpider):
    name = 'chinanews'
    start_urls = ['http://www.chinanews.com/rss/rss_2.html']

    rules = (
        Rule(LinkExtractor(allow=('.*?\.xml',)), callback='parse_items'),
    )

    def parse_items(self, response):
        selector = Selector(response)
        for node in selector.xpath('//item'):  ##//的意思：从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置
    ##你妈的，这里selector.xpath('//item')不用再加.extract(),加了就直接把节点内容直接提取为str格式。！！！
            item = NewsFeedItem()
            item['title'] = node.xpath('title/text()').get()  ##这里不用extract_first(),新版本用get()更好
            item['link'] = node.xpath('link/text()').get()
            item['desc'] = node.xpath('description/text()').get()
            item['pub_date'] = node.xpath('pubDate/text()').get()

            yield item
