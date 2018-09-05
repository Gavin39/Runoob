# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import os

class RunoobPipeline(object):

    def process_item(self, item, spider):
        #获取当前工作目录
        base_dir = os.getcwd()
        #文件存储地址
        filename = base_dir + "\\runoob.json"

        with open(filename,"a",encoding="utf-8") as fileStream:
            line = json.dumps(dict(item),ensure_ascii=False)+",\n"
            fileStream.write(line)
        return item
