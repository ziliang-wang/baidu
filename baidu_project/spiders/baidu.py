import json

import scrapy

from baidu_project.items import BaiduProjectItem


class BaiduSpider(scrapy.Spider):

    name = 'baidu'

    def start_requests(self):
        kw = input('请输入关键字: ')
        for i in range(0, 150, 30):
            url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj' \
                  '&ct=201326592&is=&fp=result&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&l' \
                  'm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest' \
                  '=&copyright=&word={}&s=&se=&tab=&width=&hei' \
                  'ght=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=girl&p' \
                  'n={}&rn=30&gsm=1e&1588049900310='.format(kw, i)
            yield scrapy.Request(url)

    def parse(self, response):
        item = BaiduProjectItem()
        json_dict = json.loads(response.text)
        for data in json_dict['data']:
            if data:
                print('正在下载图片......', data['thumbURL'])
                item['image_urls'] = [data['thumbURL']]
                yield item

