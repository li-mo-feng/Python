dic={'name':'淡淡','sex':'男','professional':'计算机科学与技术'}
dic['zhangsan']='李四'
# 新增
dic['zhangsan']='王五'
# 修改
del dic['name']
sorted(dic,)
print(dic)w

# 字典排序
d = {'a': 1, 'g': 4, 'c': 2, 'b': 12}
list1=sorted(d.items(),key=lambda x:x[0])
print(list1)


lis2=[1,2,4.7,3,10]
lis2.sort()