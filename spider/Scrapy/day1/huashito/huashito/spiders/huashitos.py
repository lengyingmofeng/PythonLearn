import scrapy
from huashito.items import HuashitoItem
from pyasn1.compat.octets import null


class HuashitosSpider(scrapy.Spider):
    name = 'huashitos'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.huashi6.com/hot']
    new_url = 'https://www.huashi6.com/hot_%d'
    page_num = 2

    def parse(self, response):
        list_div = response.xpath('//div[@class="px-waterfall fl"]')
        for div in list_div:
            img_src = div.xpath('.//div[@class="c-work-img"]/img/@src').extract_first()
            img_alt = div.xpath('.//div[@class="c-work-img"]/img/@title').extract_first()
            renqi = div.xpath('.//div[@class="like"]/span/text()').extract_first()
            item = HuashitoItem()
            item['http'] = img_src
            item['name'] = img_alt
            item['renqi'] = renqi
            yield item
        if self.page_num < 30:  # 分页
            new_url = format(self.new_url % self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url, callback=self.parse)
