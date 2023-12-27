# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import pymysql
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class ImagePipeline(ImagesPipeline):
    count = 0
    def get_media_requests(self, item, info):
        #print('thumb:' + item['thumb'])
        yield Request(item['image'], meta={'name_id': item['name_id']})

    def file_path(self, request, response=None, *, info=None):
        file_name = request.meta['name_id']
        file_name = file_name + '.jpg'
        print('filename:' + file_name)
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            item['image'] = 'none'

        return item



class MysqlPipeline:
    def __init__(self, host, db, user, password, port):
        print('mysql init:'+host)
        self.host = host
        self.db = db
        self.user = user
        self.password = password
        self.port = port
        self.database = pymysql.connect(self.host, self.user, self.password, self.db, charset='utf8',
                                        port=self.port)
        self.cursor = self.database.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            db=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT')
        )

    def open_spider(self, spider):
        print('打开MySQL爬虫')


    def close_spider(self, spider):
        print('关闭MySQL爬虫')
        self.database.close()

    def process_item(self, item, spider):
        print(item['name'])
        data = dict(item)
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s)' % ('fang', keys, values)
        print(sql)
        self.cursor.execute(sql, tuple(data.values()))
        self.database.commit()
        return item

class BiqugePipeline:
    def __init__(self):
        self.fb = open('content.json', 'w+', encoding='utf-8')

    def open_spider(self, spider):
        print('打开爬虫')

    def process_item(self, item, spider):
        print(item)
        res = dict(item)
        item_json = json.dumps(res, ensure_ascii=False)
        self.fb.write(item_json + '\n')
        return item

    def close_spider(self, spider):
        self.fb.close()
        print('关闭爬虫')
