"""
高性能异步爬虫
目的：在爬虫中使用异步实现高性能的数据爬取操作

异步爬虫的方式：
    -多线程，多进程：(不建议)
        好处：可以为相关阻塞的操作单独开启线程或者进程，阻塞操作可以就可以异步执行
        弊端：无法无限制的开启多线程或者多进程
    -线程池，进程池：(适当使用)
        好处：我们可以降低系统对进程或者线程创建和销毁的一个频率，从而很好的降低系统的开销
        弊端：池中线程或数量是有上限
"""
import requests
urls=[
    "https://www.shangmayuan.com/a/f58d1b64c435433f86c44312.html",
    "https://www.baidu.com/s?ie=UTF-8&wd=requests.exceptions.InvalidURL%3A%20Proxy%20URL%20had%20no%20scheme,%20should%20start%20with%20http%3A//%20or%20https%3A//",
    "https://www12.baidu.com/"
]
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38"
}
def get_content(url):
    print("正在爬取:",url)
    response=requests.get(url=url,headers=headers)
    if response.status_code==200:
        return response.content

def parse_content(content):
    print('相应数据的长度为:',len(content))

for url in urls:
    content = get_content(url)
    parse_content(content)