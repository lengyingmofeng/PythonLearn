# _*_ coding: utf-8 _*_

__author__ = 'jt'
__date__ = '2020/11/13 16:09'

import re
import scrapy
from scrapy.http import Request
from biquge.items import BiqugeItem


class MySpider(scrapy.Spider):
    name = 'biquge'
    base_url = 'http://localhost/output/https@sy.ke.com/ershoufang/pg'
    end_url = '.htm'
    page = ''

    def start_requests(self):
        self.page = '3'
        url = self.base_url + self.page + self.end_url
        yield Request(url, self.parse)

    def parse(self, response):
        url = self.base_url + self.page + self.end_url
        print("url::" + url)
        yield Request(url, callback=self.get_name, dont_filter=True)

    def get_name(self, response):
        pattern = re.compile('<li class="clear">.*?href="(.*?)".*?'
                             + 'data-original="(.*?)".*?'
                             + 'alt="(.*?)".*?'
                             + '<div class="positionInfo">.*?<a.*?">(.*?)</a>.*?</div>.*?'
                             + '</li>', re.S)

        # print(response.text)
        items = re.findall(pattern, response.text)

        for item in items:
            print(item)
            link = item[0]
            image = item[1]
            name = item[3]

            # 处理name_id
            pat1 = re.compile('https://sy.ke.com/ershoufang/(.*?).html', re.S)
            ids = re.findall(pat1, link)
            name_id = ids[0]
            yield Request(link, callback=self.get_chapterurl,
                          meta={'name': name, 'link': link,
                                'name_id': name_id})

    def get_chapterurl(self, response):
        print(response)
        item = BiqugeItem()
        item['name'] = str(response.meta['name'])
        item['link'] = str(response.meta['link'])
        item['name_id'] = str(response.meta['name_id'])
        return item
