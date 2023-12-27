# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter

# class ImgproPipeline:
#     def process_item(self, item, spider):
#         return item

from scrapy.pipelines.images import ImagesPipeline
import random

class imgsPileLine(ImagesPipeline):
    s = 1

    def get_media_requests(self, item, info):        # 就是可以根据图片地址进行图片数据的请求
        yield scrapy.Request(item['src'])

    # 制定图片的存储的路径
    def file_path(self, request, response=None, info=None, *, item):
        img_Name = str(self.s) + item['alt'] + '.png'
        print(img_Name, "下载成功")
        self.s += 1
        return img_Name

    def item_completed(self, results, item, info):
        return item

