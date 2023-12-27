import scrapy
from Scrapy.items import ScrapyItem

class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']
    # 基于终端制定的存储化过程
    # def parse(self, response):
    #     div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
    #     all_data = []
    #     for div in div_list:
    #         author = div.xpath('.//div[@class="author clearfix"]/a[2]/h2/text()').extract_first()
    #         content = div.xpath('.//div[@class="content"]/span//text()').extract()
    #         content = "".join(content)
    #         dic = {
    #             'author': author,
    #             'content': content
    #         }
    #         all_data.append(dic)
    #     return all_data

    # 基于管道
    def parse(self, response):
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        all_data = []
        for div in div_list:
            author = div.xpath('.//div[@class="author clearfix"]/a[2]/h2/text()').extract_first()
            content = div.xpath('.//div[@class="content"]/span//text()').extract()
            content = "".join(content)

            item = ScrapyItem()
            item['author'] = author
            item['content'] = content
            # 将item提交给了管道
            yield item
