# 要求音乐文件夹下面你的音乐文件中的MP3的名字的音乐写入到TXT文本
#
#
# 首先需要定义函数
# 先读取主目录下的文件是否是空
# 如果是空那么打印出文件名
# 如果不是空那么判断文件是否是文档,如果是文档那么获取文件名并打印
# 如果不是文档,那么将下级目录假如到需要判断的路径列表中,再进行判断下级目录中的文件是否是空,并重复这个过程
#
#
#

import os
import collections
path="E:\音乐"
list=[path]
# print(list)
while len(list)!=0:#当文件列表不是空的时候从列表末端取出一个路径地址
    path=list.pop()
    if os.path.isfile(path):
        print("文档是:"+path)
    else:
        name=os.listdir(path)#在这里name是个列表,是下级文件的文件名列表,所以需要遍历
        for i in name:
            path1=os.path.join(path,i)
            list.append(path1)