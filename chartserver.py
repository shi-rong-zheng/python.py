# 这是一个服务端程序
#双向管道流(socket)
"""
from socket import *
import threading
#创建服务器端的socket管道
serversocket=socket(AF_INET,SOCK_STREAM)
print('[测试消息]:创建服务器对象成功...')

#绑定地址对象，类似于给一部手机装电话卡
serversocket.bind(('localhost',9999))

#为服务器监听
serversocket.listen(5)
print('[测试消息]:服务器正在监听客服端连接...')

'''  执行程序   '''
while True:
    #接收客户端发送过来的连接
    #通过本函数可以得到两个返回值
    #conn是连接对象
    #addr是连接对象的地址
    conn,addr=serversocket.accept()
    print('[测试消息]:一个用户{0}上线，连接编号为:{1}'.format(conn.getsockname(),conn.fileno()))
"""

from socket import *
import threading
#创建服务器端的socket管道
chartserver=socket(AF_INET,SOCK_STREAM)
print('[测试消息] 创建服务器对象成功...')

#绑定地址对象，类似于给一部手机装电话卡
conn=chartserver.bind(('localhost',9999))

#为服务器监听
chartserver.listen(5)
print('[测试消息] <<<客户端连接成功>>>')

#创建存储用户昵称的字典
mydict=dict()

#创建存储所有在线用户的列表
mylist=list()

'''消息广播的函数，用于接收客户端的消息，然后把该消息广播给其他所有在线用户'''
def broadcastData(connNum,msg):
    #创建一个循环，用于迭代所有的在线客户
    for conn in mylist:
        #需要排除掉消息的发送者
        if conn.fileno()!=connNum:
            try:
                conn.send(msg.encode('utf-8'))
            except:
                pass

'''用于处理上线用户和服务器端通信的功能'''
def subThreadIn(conn,connNum):
    #获取到上线客户端设置的昵称
    nickname=conn.recv(1024).decode('utf-8')
    #把该昵称存储到字典中
    #用conn.fileno()作为唯一的key
    #用nickname作为value
    mydict[conn.fileno()]=nickname

    #把用户存储到在线客户列表
    mylist.append(conn)
    print('[测试消息] 客户端:{0},昵称为:{1}'.format(connNum,nickname))

    #要把某人上线的信息广播给其它所有用户
    broadcastData(connNum,'[系统信息]:'+mydict[connNum]+'进入聊天室')

    #创建一个循环，用于于客户端保持持久通信
    while True:
        try:
            #接收客户端发来的信息
            recvMsg=conn.recv(1024).decode('utf-8')

            if recvMsg:
                print('[测试消息] ',mydict[connNum],':',recvMsg)
                #需要把某个用户说的话广播给其它所有在线用户
                broadcastData(connNum,mydict[connNum]+':'+recvMsg)
            else:
                pass
        except(OSError,ConnectionResetError):
            try:
                #客户端掉线了，则从在线客户列表中删除掉
                mylist.remove(conn)
            except:
                pass
            print('[测试消息] {0}下线，当前在线人数为:{1}'.format(mydict[connNum],len(mylist)))

            # 把某人下线的消息广播给其它所有在线用户
            broadcastData(connNum, '[系统消息] ' + mydict[connNum] + ' 下线')

            #关闭掉连接
            conn.close()

            return
''' 执行程序 '''
while True:
    # 接收客户端发送过来的连接
    # 通过本函数可以得到两个返回值
    # conn 是连接对象
    # addr 是连接对象的地址
    conn,addr=chartserver.accept()
    print('[测试消息] 一个用户{0}上线，连接编号为:{1}'.format(conn.getsockname(),conn.fileno()))

    try:
        #接收客户端发来的消息
        msg=conn.recv(1024).decode('utf-8')

        # 如果客户端发送过来的是'1'，则显示'欢迎'
        if msg=='1':
            conn.send(b'huan ying jin ru liao tian shi')
            #将连接对象创建为线程对象

            mythread=threading.Thread(target=subThreadIn,args=(conn,conn.fileno()))
            #把该线程对象设置为后台线程
            mythread.setDaemon(True)
            #启动该线程
            mythread.start()

        else:
            conn.send(b'lian jie shi bai')
            conn.close()

    except:
        pass



"""
import socket
try:
    s=socket.socket()
    host=socket.gethostname()
    port=1234
    s.bind((host,port)) #绑定
    s.listen()#监听
    print(host,'正在监听')
    while True:
            c=s.accept()[0]
            d=c.recv(1024)#接受端口
            d=d.decode()

            d='史荣政想对你说:'+d
            d=d.encode()

            c.send(d)
            c.close()
    s.close()
except Exception as e:
    print(e)
"""




















