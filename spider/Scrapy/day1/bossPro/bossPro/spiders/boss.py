import scrapy
from bossPro.items import BossproItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']

    start_urls = ['https://mip.chazidian.com/lizhigushi/']

    def parse_detail(self, response):
        item = response.meta['item']
        p = response.xpath('///*[@id="showmore"]/p/text()').extract()
        p = "".join(p)
        item['p'] = p
        yield item

    def parse(self, response):
        list_li = response.xpath('/html/body/div[7]/ul/ul/li')
        for li in list_li:
            item = BossproItem()
            title = li.xpath('./a/text()').extract()
            title = "".join(title)
            item['title'] = title
            skt = li.xpath('./a/@href').extract_first()
            yield scrapy.Request(skt, callback=self.parse_detail, meta={'item': item})
