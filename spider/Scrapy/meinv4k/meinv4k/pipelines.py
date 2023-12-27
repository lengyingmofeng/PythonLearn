# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from . import settings


class Meinv4KPipeline:
    def process_item(self, item, spider):
        return item


class BeikePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_src'])

    def file_path(self, request, response=None, info=None, *, item=None):
        page = item['page']
        # 存储文件路径目录
        img_source = settings.IMAGES_STORE
        img_path = img_source + "/" + page
        print(img_path)
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        img_name = img_path + "/" + item['img_name']
        # img_name = item['img_name']
        print(img_name, "下载成功")
        return img_name

    def item_completed(self, results, item, info):
        return item
