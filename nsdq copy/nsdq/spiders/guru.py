# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from nsdq.items import GuruItem
import pandas as pd
import re




class GuruSpider(CrawlSpider):
    name = 'guru'
    allowed_domains = ['nasdaq.com']
    #start_urls = ['http://nasdaq.com/']

    #rules = (
    #    Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    #)

    def start_requests(self):
        n_stock = getattr(self, 'n_stock', 2)
        n_stock=int(n_stock)
        nsdqDF = pd.read_csv("http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=%s&render=download")
        urls = nsdqDF.ix[:n_stock, 8]
        # urls=nsdqDF.ix[:2,8]
        for url in urls:
            guru_url = url + "/guru-analysis"
            yield scrapy.http.Request(url=guru_url, callback=self.parse)

    def parse(self, response):
        # item = Myitem()
        percentage_list = response.xpath("//a[@href]/b/text()").extract()
        pattern = re.compile(r'\d{1,}')
        score_list = [int(pattern.match(i).group()) for i in percentage_list]
        #symbol = response.xpath("//div[@class='qwidget-symbol']/text()").re_first(u'(\w+)\s')
        symbol = response.url.split('/')[-2]
        item = GuruItem(symbol=symbol, scorecard=score_list)
        return item