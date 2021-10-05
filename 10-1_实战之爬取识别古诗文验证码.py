# 实战：识别古诗文网登录页面中的验证码
# 使用打码平台识别验证码的编码流程：
# 1.将验证码图片进行本地下载
# 2.调用平台提供的实例代码进行图片数据识别
import requests
from hashlib import md5
from lxml import etree
import os

#封装识别验证码图片的函数
# def getCodeText():
class Chaojiying_Client(object):

		def __init__(self, username, password, soft_id):
			self.username = username
			password = password.encode('utf8')
			self.password = md5(password).hexdigest()
			self.soft_id = soft_id
			self.base_params = {
				'user': self.username,
				'pass2': self.password,
				'softid': self.soft_id,
			}
			self.headers = {
				'Connection': 'Keep-Alive',
				'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
			}

		def PostPic(self, im, codetype):
			"""
			im: 图片字节
			codetype: 题目类型 参考 http://www.chaojiying.com/price.html
			"""
			params = {
				'codetype': codetype,
			}
			params.update(self.base_params)
			files = {'userfile': ('ccc.jpg', im)}
			r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
							  headers=self.headers)
			return r.json()

		def ReportError(self, im_id):
			"""
			im_id:报错题目的图片ID
			"""
			params = {
				'id': im_id,
			}
			params.update(self.base_params)
			r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
			return r.json()


if __name__=="__main__":
	#1.将验证码图片下载到本地
	url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38"
	}
	#获取页面源码数据
	page_text=requests.get(url=url,headers=headers).text
	#实例化一个对象，解析验证码图片img中src属性值
	tree=etree.HTML(page_text)
	#解析到图片的地址
	url_src="https://so.gushiwen.cn"+tree.xpath('//div[@class="mainreg2"]/div[4]//img/@src')[0]
	#获取图片二进制的数据
	page_src=requests.get(url=url_src,headers=headers).content
	#创建一个文件夹
	if not os.path.exists('./yanzhengma'):
		os.mkdir('./yanzhengma')
	Path=url_src.split('/')[-1]+".jpg"
	imgPath='./yanzhengma/'+Path
	with open(imgPath,"wb") as fp:
		fp.write(page_src)
		# print(Path,"爬取成功！！！")

	#调用打码平台的示例程序进行验证码图片数据识别
	chaojiying = Chaojiying_Client('13096811221', 'srz1718744251', '916870')	#用户中心>>软件ID 生成一个替换 96001
	im = open('./yanzhengma/RandCode.ashx.jpg', 'rb').read()										#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
	print("验证码:"+chaojiying.PostPic(im, 1902)['pic_str'])









































































