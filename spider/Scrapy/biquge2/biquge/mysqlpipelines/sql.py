# _*_ coding: utf-8 _*_

__author__ = 'jt'
__date__ = '2020/11/14 9:35'

import pymysql
from scrapy.utils.project import get_project_settings
settings = get_project_settings()

class BiqugePipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(settings['MYSQL_HOST'], settings['MYSQL_USER'],
                                    settings['MYSQL_PASSWORD'], settings['MYSQL_DB'])
