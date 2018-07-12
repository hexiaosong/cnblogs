# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import os
import json
import codecs
from datetime import datetime


class JsonWithEncodingCnblogsPipeline(object):
    def __init__(self):

        if os.path.exists('/data'):
            self.path = '/data/cnblog.json'
        else:
            self.path = 'cnblog.json'

        self.file = codecs.open(self.path, 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
