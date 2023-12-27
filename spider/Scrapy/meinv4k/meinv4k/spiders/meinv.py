import scrapy


class MeinvSpider(scrapy.Spider):
    name = 'meinv'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://pic.netbian.com/4kmeinv/']
    # 生成一个通用的url模板
    url = "https://pic.netbian.com/4kmeinv/index_%d.html"
    page_num = 2  # 控制网站页面页数，一般网站第一页没有后缀，所以我们默认第二页添加

    def parse(self, response):
        list_li = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in list_li:
            title = li.xpath('./a/b/text()').extract_first()
            print(title)

        if self.page_num < 10:
            new_url = format(self.url % self.page_num)  # 网站拼接
            self.page_num += 1

            # 手动的请求发送：callback回调函数是专门用于数据解析
            yield scrapy.Request(url=new_url, callback=self.parse)
