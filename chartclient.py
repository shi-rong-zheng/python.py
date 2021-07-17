
#客户端程序

from socket import *
import threading

#创建连接对象
clientsocket=socket(AF_INET,SOCK_STREAM)

#建立连接
clientsocket.connect(('localhost',9999))

#客户端向服务端发送消息
clientsocket.send(b'1')

#接收服务器端发来的数据
print(clientsocket.recv(1024).decode('utf-8'))  #recv(1024)缓存大小

#向服务器端发送昵称
nickname=input('输入昵称:')

#向服务器端发送的是utf-8编码的昵称
clientsocket.send(nickname.encode('utf-8'))

'''向服务器端发送消息的功能'''
def sendThreadFun():

    #使用循环就是为了消息的功能
    while True:
        try:
            #写消息
            msg=input('--->:')
            #把消息发送到服务器端
            clientsocket.send(msg.encode('utf-8'))
        except ConnectionAbortedError:
            print('服务器端断开了连接')
        except ConnectionResetError:
            print('服务器已关闭')

'''接收服务器端的信息'''
def recvThreadFun():
    #使用循环可以接收到服务器端发来的信息
    while True:
        try:
            recvmsg=clientsocket.recv(1024)
            #打印输出信息给用户看
            if recvmsg:
                print(recvmsg.decode(('utf-8')))
        except ConnectionAbortedError:
            print('服务器端断开了练习')
        except ConnectionResetError:
            print('服务器已关闭')

#创建出发送消息的线程对象
sendThread=threading.Thread(target=sendThreadFun)
#创建出接收信息的线程对象
recvThread=threading.Thread(target=recvThreadFun)

#如果以后需要启动的线程比较多，则可以将需要启动的线程加入到一个列表中
threads=[sendThread,recvThread]

#通过循环启动线程运行
for t in threads:
    #将线程对象设置为后台线程，也叫作 精灵线程，守护线程
    t.setDaemon(True)
    #启动线程
    t.start()
t.join()

"""
#服务端程序(收，发消息)
import socket
import struct
def readInt(socket):
    size=struct.calcsize('@i')
    data=socket.recv(size)
    n=struct.unpack('@i',data)[0]
    return n
def writeInt(socket,n):
    data=struct.pack('@i',n)
    socket.send(data)

def readString(socket):
    size=struct.calcsize('@i')
    d=socket.recv(size)
    n=struct.unpack('@i',d)[0]
    data=socket.recv(n)
    return data.decode('utf-8')

def writeString(socket,s):
    data=s.encode('utf-8')
    size=len(data)
    d=struct.pack('@i',size)
    socket.send(d)
    socket.send(data)

try:
    s=socket.socket()
    host=socket.gethostname()
    port=2345
    s.bind((host,port))
    s.listen()
    print(host,'在监听...')
    c=s.accept()[0]
    fileName=readString(c)
    print('文件名字',fileName)
    size=readInt(c)
    print('文件尺寸',size)
    data=b""
    while len(data)<size:
        d=c.recv(size)
        if len(d)>0:
            data=data+d
        else:
            break
    fobj=open(fileName,'wb')
    fobj.write(data)
    fobj.close()
    print('上传成功！')
    writeString(c,'OK')

    c.close()
    s.close()
except Exception as e:
    print(e)
"""




"""
#client
from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from  PyQt5.QtWidgets import *
import sys
from socket import *
from threading import Thread

class Client(QWidget):
    #初始化界面
    def __init__(self):
        QWidget.__init__(self)
        #设置窗口的大小与位置
        self.setGeometry(600,300,360,300)
        #设置标题
        self.setWindowTitle('聊天室')
        #添加背景
        palette=QtGui.QPalette()
        bg = QtGui.QPixmap(r'./qiutulibs/1DCS8SM8MSN9XLZH.jpg')
        palette.setBrush(self.backgroundRole(),QtGui.QBrush(bg))
        self.setPalette(palette)
        self.add_ui()

        # 与服务器链接
        self.client=socket(AF_INET,SOCK_STREAM)
        self.client.connect(('127.0.0.1',8888))
        # 调用线程
        self.work_thread()        #     设置界面组件
    #设置界面中的组件
    def add_ui(self):
        #多行文本显示，显示所有的聊天信息
        self.content = QTextBrowser(self)
        self.content.setGeometry(30,30,300,150)

        #单行文本，信息发送框
        self.message=QLineEdit(self)
        self.message.setPlaceholderText(u'请输入发送内容')
        self.message.setGeometry(30,200,300,30)

        #发送按钮
        self.button = QPushButton('发送', self)
        self.button.setFont(QFont('微软雅黑', 10, QFont.Bold))
        self.button.setGeometry(270, 250, 60, 30)

        #发送消息

    def send_msg(self):
        msg = self.message.text()
        self.client.send(msg.encode())
        if msg.upper() == QtGui:
            self.client.close()
            self.destroy()
        self.message.clear()

        #     接受消息

    def recv_msg(self):
        while True:
            try:
                data = self.client.recv(1024).decode()
                print(data)
                data = data +'\n'
                self.content.append(data)
            except:
                exit()

    def btn_send(self):
        self.button.clicked.connect(self.send_msg)

        #     匿名类，线程处理,发送是一个线程，接受是一个线程

    def work_thread(self):
        Thread(target=self.btn_send).start()
        Thread(target=self.recv_msg).start()

if __name__=='__main__':
    app=QApplication(sys.argv)
    Client=Client()
    Client.show()
    sys.exit(app.exec())

"""



"""
import socket
input('按任意键开始链接服务器...')
try:
    s=socket.socket()
    host=socket.gethostname()
    port=1234
    s.connect((host,port))
    print('客户端链接成功！！！')
    d=input('请输入你要发送的字符串:')
    d=d.encode()
    s.send(d)
    d=s.recv(1024)
    d=d.decode()
    print(d)
    s.close()

except Exception as e:
    print(e)
"""


"""
#客户端程序(发,收消息)
import socket
import struct
import os

def readInt(socket):
        size=struct.calcsize('@i')
        data=socket.recv(size)
        n=struct.unpack('@i',data)[0]
        return n

def writeInt(socket,n):
        data=struct.pack('@i',n)
        socket.send(data)

def readString(socket):
        size=struct.calcsize('@i')
        d=socket.recv(size)
        n=struct.unpack('@i',d)[0]
        data=socket.recv(n)
        return data.decode('utf-8')

def writeString(socket,s):
        data=s.encode('utf-8')
        size=len(data)
        d=struct.pack('@i',size)
        socket.send(d)
        socket.send(data)

try:
       fileName=input('上传文件路径名称:')
       if os.path.exists(fileName):
           fobj=open(fileName,'rb')
           data=fobj.read()
           fobj.close()
           p=fileName.rfind('\\')
           fileName=fileName[p+1:]
           size=len(data)
           print('文件名称:',fileName)
           print('文件尺寸:',size)
           s=socket.socket()
           host=socket.gethostname()  
           port=2345
           s.connect((host,port))
           writeString(s,fileName)
           writeString(s,size)
           s.send(data)
           resp=readString(s)
           if resp=='OK':
                   print('上传成功！')
           else:
                   print('上传失败！')  
           s.close()
       else:
               print(fileName+'不存在！')

except Exception as e:
    print(e)
"""






