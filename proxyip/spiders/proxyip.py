#-*- coding = utf-8 -*-
__author__ = 'wangxinagyang'
#create by 2017-12-07

import scrapy
import os
import requests
from bs4 import BeautifulSoup
import json
from ..items import ProxyipItem

class Proxyip(scrapy.Spider):
    name = 'proxyip'
    start_urls = ['http://www.xicidaili.com/nn/{}'.format(i) for i in range(1,10)]

    #start parser
    def parse(self, response):
        tbody = response.xpath('//*[@id="ip_list"]')[0]
        trs = tbody.xpath('//tr')[1:]
        item = [ ]
        for tr in trs:
            item_pre = ProxyipItem()
            item_pre['ip'] = tr.xpath('td[2]/text()').extract()[0]
            #print item['ip']
            item_pre['port'] = tr.xpath('td[3]/text()').extract()[0]
            #print item['port']
            item_pre['address'] = tr.xpath('string(td[4])').extract()[0].strip()
            #print item['address']
            item_pre['type_id'] = tr.xpath('td[6]/text()').extract()[0]
            #print item['type_id']
            item_pre['speed'] = tr.xpath('td[7]/div/@title').re('\d+\.\d*')[0]
            #print item['speed']
            item_pre['proving_time'] = tr.xpath('td[10]/text()').extract()[0]
            #print item['proving_time']
            item.append(item_pre)
            #print item
        return item





