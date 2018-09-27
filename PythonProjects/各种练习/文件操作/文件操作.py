path="file/book"
file=open(path,"r",encoding='utf-8')
# 文件操作首先需要打开目标文件
str=file.read()
# 文件读取，仅当文件内容小于内存时
str1=file.readlines()
# 文件读取，将内容分解为以行为单位的列表
print(str)
file.close()