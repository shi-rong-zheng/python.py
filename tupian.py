import scrapy
from tupianPro.items import TupianproItem

class TupianSpider(scrapy.Spider):
    name = 'tupian'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_lsit = response.xpath('//*[@id="container"]/div')
        for div in div_lsit:
            # 注意：使用为属性（图片软加载）
            src = 'https:' + div.xpath('./div/a/img/@src2').extract_first()
            item=TupianproItem()
            item['src']=src
            yield item
