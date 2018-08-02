__author__ = 'solteee'

import scrapy
from community.items import bookItem

class YesSpider(scrapy.Spider):
    name = "yes24"
    allowed_domains = ["www.yes24.com"]
    start_urls = [
        "http://www.yes24.com/searchcorner/Search?keywordAd=&keyword=&domain=ALL&qdomain=%C0%FC%C3%BC&Wcode=001_005&query=crawling="
    ]

    def parse(self, response):
        for sel in response.xpath('//td[re:test(@class, "goods_infogrp")]/p[re:test(@class, "goods_name goods_icon")]/a'):
            item = bookItem()
            item['title'] = sel.xpath('strong/text()').extract()
            item['link'] = sel.xpath('@href').extract()
            yield item



