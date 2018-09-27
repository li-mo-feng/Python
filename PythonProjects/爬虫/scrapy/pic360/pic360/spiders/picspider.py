from scrapy.spider import CrawlSpider
import json
from scrapy.selector import Selector
import scrapy
from scrapy import Request
from ..items import Pic360Item

class pics(CrawlSpider):
    name = 'pics'
    start_urls=['http://image.so.com/zj?ch=beauty']
    url="http://image.so.com/zj?ch=beauty&sn=30&listtype=new&temp=1"

    def parse(self, response):
        item=Pic360Item()
        result=json.loads(response.text)
        for list in result.get('list'):
            # 获得其中的列表信息让后遍历
            # 得到的结果是图片的地址列表
            yield item['IMAGES_STORE'].append(list['qhimg_url'])






    # def download(self,response):
    #     base_url='http://image.so.com/zj?ch=beauty'
    #     for page in range(1,5):
    #         sn=str(page*30)
    #         url=base_url+sn
    #         yield response(url)

