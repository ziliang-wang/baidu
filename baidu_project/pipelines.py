# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

import scrapy
from scrapy.pipelines.images import ImagesPipeline


class BaiduProjectPipeline(object):
    def process_item(self, item, spider):
        return item


class BaiduImagesPipeline(ImagesPipeline):

    idx = 1

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,
                                 meta={'idx': self.idx})
            self.idx += 1

    def file_path(self, request, response=None, info=None):
        idx = request.meta['idx']
        file_name = re.sub(r'.*?(\d)\.jpg', str(idx).zfill(8), request.url) + '.jpg'
        return file_name

