"""
代理：
破解封IP这种反爬机制。
什么是代理：
    -代理服务器
代理的作用：
    -图片自身IP访问的限制
    -隐藏自身真实IP
代理相关的网站：
    -西拉免费代理IP(http://www.xiladaili.com/gaoni/)
代理ip的类型：
    -http：应用到http协议对应的url中
    -https：应用到https协议对应的url中
代理ip的匿名度：
    -透明：服务器知道该次请求使用了代理，也知道请求对应的真实ip
    -匿名：知道使用了代理，不知道使用真实ip
    -高匿，不知道使用了代理，更不知道真实的ip


"""
import requests
url="https://www.so.com/s?ie=utf-8&src=hao_360so_b_cube&shb=1&hsid=abca92474cd310e6&q=ip"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}
response=requests.get(url=url,headers=headers,proxies={"http":"http://119.114.21.44:9999"},verify=False)
response.encoding='utf-8'
page_text=response.text
# print(page_text)
with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)
































