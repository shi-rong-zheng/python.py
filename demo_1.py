'''
这是第一行注释
'''
# print("hello,world")
# a=10
# print(a)

# age=18
# print("我的名字是%s,我的国籍是%s"%("小智","中国"))
# print("我的年龄是：%d岁"%age)
# print("aaa","bbbb","vvv")
# print("www","baidu","com",sep=".")#sep分割、
# print("world",end="")
# print("python",end="\t")
# print("java",end="\n")
# print("end")

# password=input("请输入密码：")
# print("你输入的密码是:",password)

# password = input("请输入密码：")
# print(type(password))


# if True:
#     print("True",end=" ")
#     print("ag")
# else:
#     print("false")
# print("end")

# score=77
# if score>=90:
#     print("A")
# elif score>70 and score<90:
#     print("B")
# else:
#     print("C")

# import random #random 随机数
# x=random.randint(0,9)
# print(x)

# for i in range(1,20,3):
#     print(i,end=" ")

# name="shirongzheng"
# for x in name:
#     print(x,end='')

# name=["aa","bb","cc"]
# for i in range(len(name)):
#     print(i,name[i])

# i=1
# sum=0
# while i<=100:
#     sum+=i
#     i=i+1
# print(sum)

# count=0
# while count<5:
#     print(count,"小于5")
#     count+=1
# else:
#     print(count,"大于或等于5")

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(i,j,i*j),end=' ')
#     print("\n")



# i=1
# while i<10:
#     j = 1
#     while j<=i:
#         print("%d*%d=%d"%(i,j,i*j),end=" ")
#         j=j+1
#     print(" ")
#     i = i + 1

# str="chengdu"
# print(str)
# print(str[0:5:2])


# namelist=[]
# namelist=["小张","小王","小李"]
# # print(namelist[2])
# print("----增加前-----")
# for i in range(len(namelist)):
#     print(namelist[i],end=" ")
# print("\n")
# print("----增加后-----")
# namelist.append("小史")
# for i in range(len(namelist)):
#     print(namelist[i],end=" ")

# a=[1,2]
# b=[3,4]
# a.extend(b)  #将b列表中每个元素，逐一加入a列表中
# print(a)


# a=[0,1,2]
# a.insert(1,3)  #某一个变量表示下标，某二哥表示元素（对象
# print(a)

#删 【del】 【remove】 【pop】
# moviename=["加勒比海盗","黑客帝国","某一滴血","指环王","速度与激情"]
# print("----删除前-----")
# for i in moviename:
#     print(i,end=" ")
# print("\n")
# print("----删除后-----")
# del moviename[2]      #删除指定的某一个元素
# for i in moviename:
#     print(i,end=" ")

# moviename=["加勒比海盗","黑客帝国","某一滴血","指环王","速度与激情"]
# print("----删除前-----")
# for i in moviename:
#     print(i,end=" ")
# print("\n")
# print("----删除后-----")
# moviename.remove("指环王")      #删除指定的某一个元素
# for i in moviename:
#     print(i,end=" ")

# moviename=["加勒比海盗","黑客帝国","某一滴血","指环王","速度与激情"]
# print("----删除前-----")
# for i in moviename:
#     print(i,end=" ")
# print("\n")
# print("----删除后-----")
# moviename.pop()      #弹出某尾最后一个元素
# for i in moviename:
#     print(i,end=" ")

#改
# moviename=["加勒比海盗","黑客帝国","某一滴血","指环王","速度与激情"]
# print("----修改前-----")
# for i in moviename:
#     print(i,end=" ")
# print("\n")
# print("----修改后-----")
# moviename[2]="西游记"     #弹出某尾最后一个元素
# for i in moviename:
#     print(i,end=" ")

#查 ：[in , not in]
# namelist=["小张","小王","小李"]
# findName=input("请输入学生的名字:")
# if findName in namelist:
#     print("在学员名单中找到了相同的名字")
# else:
#     print("没有找到")

# a=["a","b","c","a","b"]  #可以查找指定下范围的元素，并返回找到对应数据的下
# print(a.index("a",1,4))   #范围区间，左闭右开 [1,3)   找不到会报错
#
# print(a.count("a"))

#排序和反转
# a=[1,6,74,3]
# print(a)
# a.reverse()
# print(a)
# a.sort()              #升序
# print(a)
# a.sort(reverse=True)  #降序
# print(a)

# schoolName=[["北京大学","清华大学"],["贵州大学","贵州师范大学","贵州财经大学"],["山东大学","南开大学"]]
# print(schoolName[1][2])

#实例
# import random
# offices=[[],[],[]]
# names=["A","B","C","D","E","F","G","H"]
# for name in names:
#     index=random.randint(0,2)
#     offices[index].append(name)
# i=1
# for office in offices:
#     print("办公室%d的人数为:%d"%(i,len(office)))
#     i+=1
#     for name in office:
#         print(name,end=" ")
#     print("\n")

products=[["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
print("------商品列表------")
for i in range(6):
    print("%d\t%s\t%d"%(i,products[i][0],products[i][1]))











































































