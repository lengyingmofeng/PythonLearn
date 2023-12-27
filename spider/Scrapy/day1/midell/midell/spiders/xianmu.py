import scrapy


class XianmuSpider(scrapy.Spider):
    name = 'xianmu'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wenku.baidu.com/view/89c006ea8f9951e79b89680203d8ce2f0166651e.html']

    def parse(self, response):
        page_text = response.text
        with open('ip.html', "w", encoding="utf-8") as fp:
            fp.write(page_text)