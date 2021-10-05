"""
模拟登录:
    -爬取基于某些用户信息
需求：对人人网进行模拟登录
    -点击登录按钮之后会发起一个post请求
    -post请求中会携带登录之前录入的相关登录信息（用户名，密码，验证码....）
    -验证码：每次请求都会变化
需求：爬取当前用户的相关的用户信息（个人主页中显示的用户信息）
http/https协议特性:无状态
没有请求到对应页面数据的原因：
    发起的第二次基于个人主页面请求的时候，服务器端并不知道该此请求是基于登录状态下的请求
cookie:用来让服务器端记录客户端的相关状态
    -手动处理：通过抓包工具获取cookie值，将该值封装到headers中。（不建议）
    -自动处理：
        -cookie值的来源是哪里？
            -模拟登录post请求后，由服务器端创建
        session会话对象：
            -作用：
                1.可以进行请求的发送
                2.如果请求过程中产生了cookie，则该cookie会被自动存储/携带在该session对象中
        -创建一个session对象：session=requsets。Session()
        -使用session对象进行模拟登录post请求的发送（cookie就会被存储在session中）
        -使用session对象对个人主页的get请求进行发送（携带了cookie）
"""


import requests
from lxml import etree
if __name__=="__main__":
    #网页网址
    url='https://renren.com/login?to=https%3A%2F%2Frenren.com%2F'
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38"
    }
    #获取网页的源代码
    page_text=requests.get(url=url,headers=headers).text
    #实例化一个对象，解析源码数据中的src属性值
    tree=etree.HTML(page_text)
    list_src="http://www.renren.com/"+tree.xpath('//div[@class="rr-login_code input"]/div/img/@src')[0]
    print(list_src)
    # data_img=requests.get(url=list_src,headers=headers).content
    # with open('./code.jpg','wb') as fp:
    #     fp.write(data_img)

