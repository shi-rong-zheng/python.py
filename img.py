import scrapy
from imgsPro.items import ImgsproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_lsit=response.xpath('//*[@id="container"]/div')
        for div in div_lsit:
            #注意：使用为属性（图片软加载）
            src='https:'+div.xpath('./div/a/img/@src2').extract_first()
            item=ImgsproItem()
            item['src']=src

            yield item #提交管道