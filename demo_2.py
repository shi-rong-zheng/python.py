# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


tup1 = ("abc","defg",345,67)  # 创建元组
# tup2=(50) #不是元组
# tup2 = (50,60,70)
# print(type(tup2))
# print(tup1[0])
# print(tup1[1:4])  #左闭右开，进行切片

#增
# tup1=(12,34,45)
# tup1[0]=1000   #报错
# tup2=("dfs","fgs")
# tup1=tup1+tup2
# print(tup1)
#删
# tup1=(12,34,45)
# del tup1      #删除了整个元组变量
# print("删除后:")
# print(tup1)


#字典定义
# info={"name":"吴彦祖","age":19}
# print(info["age"])
# print(info.get("gender"))        #使用get方法，没有找到对应的键，默认返回：None
# print(info.get("gender","男"))     #没有找到的时候，可以设定默认值

#字典的访问

#增
# info={"name":"吴彦祖","age":19}
# newID=input("请输入新的学号:")
# info["id"]=newID
# print(info)

#删
#[del]   删除
# info={"name":"吴彦祖","age":19}
# print("删除前:%s"%info["name"])
# del info["name"]
# print("删除后:%s"%info["name"])  #删除了指定值对后，再次访问会报错

#[clear]   清空
# info={"name":"吴彦祖","age":19}
# print("清空前:%s"%info)
# info.clear()
# print("清空后:%s"%info)

#改
# info={"name":"吴彦祖","age":19}
# info["age"]=30
# print(info["age"])

#查
info={"id":"1","name":"吴彦祖","age":19}
# print(info.keys())   #的到所有的键（列表）
#
# print(info.values())  #得到所有的值（列表）
#
# print(info.items())   #得到所有的项（列表），每个键值对是一个元组

# for key in info.keys():
#     print(key)
#
# for key in info.values():
#     print(key)

#便利所有的键值对
# for key,value in info.items():
#     print(key,":",value)

#枚举函数，同时拿到列表中的下标和元素内容
# mylist=["a","b","c","d"]
# print(enumerate(mylist))
#
# for i,x in enumerate(mylist):
#     print(i,x)

#set(集合)   去除重复值

# s=set([1,2,3])
# print(s)
#
# s1=set([1,1,2,3,5,6,5])
# print(s1)


#---------------------
#--------小结----------
'''
            是否有序         是否可变类型
列表[]       有序            可变类型
元组()       有序            不可变类型
字典{}       无序            key不可变 val可变
集合{}       无序            可变类型(不重复)
'''


#自定义函数
'''
def printinfo():
    print("-"*18)
    print("人生苦短，我用python")
    print("-"*18)
#函数调用
printinfo()
'''

#返回多个值的函数
'''
def divid(a,b):
    shang=a/b
    yushu=a%b
    return shang,yushu
sh,yu=divid(5,2)       #需要使用多个变量来接收值
print("商：%d,余：%d"%(sh,yu))
'''

'''
def printinfo():
    print("-"*10)
def suminfo(a,b,c):
    return a+b+c
printinfo()
sum=suminfo(4,5,6)
print("sum=%d"%sum)
print("average=%d"%(sum/3))
printinfo()
'''
#全局变量和局部变量
'''
a=100
def test1():
    global a   #global 全局变量的关键字
    print("tset-----修改前：a=%d" % a)
    a=300
    print("tset-----修改后：a=%d" % a)
def test2():
    print("tset-----修改后：a=%d" % a)    #没有局部变量，默认使用全局变量

test1()
test2()
'''

#文件操作
'''
f=open("./test.txt","w")   #打开文件，w模式
f.write("hello,world!!!")
f.close()  
'''


''' # read方法，读取指定的字符，开始时定位在文件头部，每执行一次向后移动指定字符数
f=open("./test.txt","r")   #打开文件，w模式
# f.write("hello,world!!!")
content=f.read()
print(content)
f.close()                  #关闭文件
# r w rb wb
'''

'''
f=open("./test.txt","r")
content=f.readlines()    #readlines  一次性读取一行
i=1
for temp in content:
    print("%d:%s"%(i,temp))
    i+=1
f.close()
'''

'''
f=open("./test.txt","r")
content=f.readline()
print("1:%s"%content,end="")
content=f.readline()
print("2:%s"%content,end="")
f.close()
'''

#文件的相关操作
'''
#文件重命名
import os
os.rename("test.txt","test-最终版.txt")
'''

'''
#删除文件
import os 
os.remove("test-最终版.txt")
'''
'''
#创建文件夹
import os
os.mkdir("./test.txt")
'''

'''
#捕获异常
try:
    print("------test--1------")
    f=open("test.txt","r")
    print("------test--2------")
except Exception as orr:        #IOError文件没有找到，属于IO异常（输入输出异常）
    print(orr)                  #Excetion可以承接所有异常
'''
'''
import time
try:
    f=open("./test.txt","w")
    f.write("hello,world!!")
    f = open("test.txt", "r")
    try:
        while True:
            content=f.readline()
            if len(content)==0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except Exception as orr:
    print(orr)
'''











































































