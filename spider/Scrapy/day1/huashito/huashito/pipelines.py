# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class HuashitoPipeline:
    con = None
    cursor = None

    def open_spider(self, spider):
        print("开始爬虫")
        self.con = pymysql.Connect(host="localhost", port=3306, user='root', password="123456", db='yefeng')

    def process_item(self, item, spider):
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute("insert into huashi values ('%d', '%s', '%s', '%s')" % (0, item['http'], item['name'], item['renqi']))
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        return item

    def close_spider(self, spider):
        self.con.close()
        self.cursor.close()
        print("结束爬虫")