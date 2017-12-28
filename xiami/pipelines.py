# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

from scrapy.exceptions import DropItem


class XiamiPipeline(object):

    def __init__(self):
        self.song_seen = set()
        self.file = codecs.open('xiamisongs.jl', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        """
        每个item pipeline组件都需要调用该方法，
        这个方法必须返回一个Item（或任何集成类）对象，
        或抛出DropItem异常，
        被丢弃的item将不被后面的pipeline处理
        :param item:
        :param spider:
        :return:
        """
        # 过滤缺失数据
        # if True:
        #   return item
        # else:
        #   raise DropItem('reason')
        if spider.name == 'Ada':
            if item['song'] in self.song_seen:
                raise DropItem('Duplicate song found: %s' % item['song'])
            else:
                self.song_seen.add(item['song'])
                '''保存到json文件(非必须)'''
                line = json.dumps(dict(item), ensure_ascii=False) + '\n'
                self.file.write(line)
                return item

    def close_spider(self, spider):
        print('spider %s is closing' % spider.name)
        self.file.close()
