# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from . import settings
import os

class HuashiproPipeline:
    fp = None
    csv_fp = None

    def __init__(self):
        self.fp = open("huashi.csv", "w", encoding='utf-8', newline='')
        self.csv_fp = csv.writer(self.fp)
        self.csv_fp.writerow(['title', 'author', 'likeNum'])

    def process_item(self, item, spider):
        title = item['title']
        author = item['author']
        likeNum = item['likeNum']
        if likeNum >= 10000:
            likeNum = round(likeNum / 10000, 1)
            likeNum = str(likeNum) + "w"
        self.csv_fp.writerow([title, author, likeNum])
        return item

    def __del__(self):
        self.fp.close()

# ImagesPipeline专门用于文件下载管道类，下载过程支持异步和多线程
class ImagesProPipeline(ImagesPipeline):

    # 对item中的图片进行请求操作
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'])

    # 指定图片存储的路径
    def file_path(self, request, response=None, info=None, *, item=None):
        imgName = request.url.split('/')[-1]
        page = item['page']
        # 存储文件路径目录
        img_source = settings.IMAGES_STORE
        img_path = img_source + os.sep + page
        print(img_path)
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        img_name = img_path + "/" + item['img_name']
        # img_name = item['img_name']
        print(img_name, "下载成功")
        print("over", imgName)
        return imgName

    # 返回给其他管道
    def item_completed(self, results, item, info):
        return item