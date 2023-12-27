import ast
import json
import re

import scrapy

from huashiPro.items import HuashiproItem


class HuashiSpider(scrapy.Spider):
    name = 'huashi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.huashi6.com/hot']
    url = 'https://rt.huashi6.com/front/works/hotlist?&index=%d'
    # 图片地址前缀
    url_prefix = "https://img2.huashi6.com/"
    page = 2

    def parse(self, response):
        obj = re.compile(r'"user".*?,(?P<worksHotListData>).*?(?P<datas>.*?);', re.S)
        html = obj.search(response.text).group('datas')
        html = "{" + html
        html = json.loads(html)  # 把数据装换成dict
        datas = html['works']['worksHotListData']['datas']
        item = HuashiproItem()
        for item in datas:
            # title = item['title']
            # author = item['painter']['name']
            # likeNum = int(item['likeNum'])
            # item['title'] = title
            # item['author'] = author
            # item['likeNum'] = likeNum
            # item['src'] = url_img
            url_img = self.url_prefix + item['coverImage']['path']
            yield item
        urls = self.url % self.page
        item['page'] = "第{}页".format(self.page)
        self.page += 1
        yield scrapy.Request(urls, self.pages_parse, meta={'item': item})

    # 爬取199页
    def pages_parse(self, response):
        item = response.meta['item']
        html = json.loads(response.text)  # 把数据装换成dict
        datas = html['data']['datas']
        for item in datas:
            title = item['title']
            author = item['painter']['name']
            likeNum = int(item['likeNum'])
            item = HuashiproItem()
            item['title'] = title
            item['author'] = author
            item['likeNum'] = likeNum
            url_img = self.url_prefix + item['coverImage']['path']
            item['src'] = url_img
            yield item
        if self.page < 50:  # 控制页数
            # url地址拼接
            urls = self.url % self.page
            # 增一添加页数
            self.page += 1
            # 请求一页的url地址
            yield scrapy.Request(urls, self.pages_parse, meta={'item': item})

    # def start_requests(self):
    #     data = {
    #         "id": "A01",
    #         "dbcode": "hgyd",
    #         "wdcode": "zb",
    #         "m": "getTree"
    #     }
    #     yield scrapy.FormRequest(url=self.start_urls[0], formdata=data, callback=self.parse)
