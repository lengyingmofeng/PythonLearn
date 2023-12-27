import scrapy
from scrapy import item
from dainying.items import DainyingItem

class DianyinSpider(scrapy.Spider):
    name = 'dianyin'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://pic.netbian.com/4kdongman/']
    new_url = "http://pic.netbian.com"

    def parse_spider(self, response):
        img_src = response.xpath('//*[@id="img"]')
        for img in img_src:
            img_data = img.xpath('./img/@src').extract_first()
            img_data = self.new_url + img_data
            item['img_data'] = img_data
            print(img_data)
            yield item

    def parse(self, response):
        div_list1 = response.xpath('//div[@class="slist"]/ul/li')
        for div in div_list1:
            item = DainyingItem()
            href = div.xpath('./a/@href').extract_first()
            href = self.new_url + href
            print(href)
            yield scrapy.Request(href, callback=self.parse_spider, meta={'item': item})
