# dict和zip的用法
# ==================
# a1=[1,2,3,'a']
# a2=[4,5,6,'b']
# ss=zip(a1,a2)
# print(ss)
# print(dict(ss))


# range（）
# 第三个参数是间隔可以理解为遍历时隔几位访问
# for i in range(5,0,-1):
#     print(i)

# coding:utf-8
# python3 -- list列表操作（拷贝copy）

# 注意文件命名方式：不能 与关键字copy等发生冲突

# 浅拷贝，只拷贝第一层，2层以上 都是拷贝元素的地址
# list_names = ["he", "li", ["liu", "li"], "fu", "chen"]
# list_names2 = list_names.copy()
# list_names2[2]='heiheihei'
# list_names[2][1]= "平"
# print(list_names)
# print(list_names2)

# 只是name，指向了list_names这个列表存储地址
# name = list_names
# print(name)
# # 多维列表：，所以2层以后的元素，会跟着原来的列表改变
# list_names[2][0] = "高"
# print(list_names)
# print(list_names2)


# 打乱列表
# import random
# a=[1,5,7,8,3]
# random.shuffle(a)
# 打乱列表顺序
# print(a)


# a=[1,2,3]
# b=[1,4,5,6]
# print(set(a)&set(b))

String="{1},{0}"
string=String.format('hello','python')
print(string)
