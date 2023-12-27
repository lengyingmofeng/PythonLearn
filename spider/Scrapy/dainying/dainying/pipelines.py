# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class DainyingPipeline:
    con = None
    cursor = None

    def open_spider(self, spider):
        self.con = pymysql.Connect(host='localhost', post=3306, user='root', password='123456', db='yefeng')

    def process_item(self, item, spider):
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute('insert into fenlei values ("%d", "%s")' % (0, item['img_data']))
            self.con.commit()
        except Exception as E:
            print(E)
            self.con.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.con.close()
