import scrapy


class QuanSpider(scrapy.Spider):
    name = 'quan'
    allowed_domains = ['www.521609.com']
    start_urls = ['http://www.521609.com/meinvxiaohua/']
    url = 'http://www.521609.com/meinvxiaohua/list12%d.html'
    page_num = 2

    def parse(self, response):
        div_list = response.xpath('//div[@class="index_img list_center"]/ul/li')
        for div in div_list:
            name = div.xpath('./a[2]/text() | ./a[2]//text()').extract_first()
            print(name)
        if self.page_num < 172:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url, callback=self.parse)