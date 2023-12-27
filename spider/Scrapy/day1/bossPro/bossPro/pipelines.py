# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class BossproPipeline:
    fp = None

    def open_spider(self, spider):
        print("开始爬虫")
        self.fp = open("励志故事.txt", "w", encoding="utf-8")

    def process_item(self, item, spider):
        title = item['title']
        p = item['p']
        self.fp.write(title + '\n' + p + "\n")
        return item

    def close_spider(self, spider):
        print("结束爬虫")
        self.fp.close()


class MysqlPipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='localhost', port=3306, user='root', password='123456', db='yefeng')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("insert into lizhi values ('%s', '%s')" % (item['title'], item['p']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
