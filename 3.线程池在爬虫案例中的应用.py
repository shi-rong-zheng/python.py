import requests
from lxml import etree
#爬取梨视频的视频数据
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38"
}
#原则：线程池处理的是阻塞且耗时的操作

#对下述url发起请求解析出视频详情页的url和视频的名称
url='https://www.pearvideo.com/'
page_text=requests.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
list_href=tree.xpath('//*[@id="vervideoTlist"]/div/ul[1]/li/div | //*[@id="vervideoTlist"]/div/ul[2]/li/div')
for a in list_href:
        href="https://www.pearvideo.com"+a.xpath('./a/@href')[0]
        name=a.xpath('./a/div[2]//div[@class="vervideo-name"]/text()')[0]+'.mp4'
        print(href+" "+name)




































