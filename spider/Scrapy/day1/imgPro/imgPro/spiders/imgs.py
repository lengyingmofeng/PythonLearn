import scrapy
from imgPro.items import ImgproItem


class ImgsSpider(scrapy.Spider):
    name = 'imgs'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.huashi6.com/hot']
    new_url = 'https://www.huashi6.com/hot_%d'
    page_num = 2

    def parse(self, response):
        i = 0
        list_fuhao = ['?', '\\', '/', '*', "'", '"', "!", '>', '<']
        div_img = response.xpath('//div[@class="waterfall clearfix px-container clear"]')
        for div in div_img:
            img_src = div.xpath('.//div[@class="px-waterfall fl"]/div/div/div/a/div/img/@src').extract()
            img_alt = div.xpath('.//div[@class="px-waterfall fl"]/div/div/div/a/div/img/@title').extract()
        for i in range(len(img_src)):
            item = ImgproItem()
            item['src'] = img_src[i]
            item['alt'] = img_alt[i]
            for element in list_fuhao:
                if item['alt'].find(element):
                    item['alt'] = "".join(item['alt'].split(element))
            yield item
        if self.page_num < 150:
            new_url = format(self.new_url % self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url, callback=self.parse)
