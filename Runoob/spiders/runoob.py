# -*- coding: utf-8 -*-
import scrapy
from Runoob.items import RunoobItem


class RunoobSpider(scrapy.Spider):

    name = "Runoob"

    allowed_domains = ["runoob.com"]

    start_urls = ["http://www.runoob.com/python3/python3-basic-syntax.html"]

    def parse(self,response):
        item = RunoobItem()
        for row in response.xpath("//div[@class='design']/a"):
            item['title'] = row.xpath("./@title").extract()[0]
            item['link'] = row.xpath("./@href").extract()[0]
            yield item