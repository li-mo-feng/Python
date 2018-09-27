import math
import random
#a=float(input("请输入任意浮点数"))
#a=random.choice(range(-100,100))#在-100到100之间的整数中随机选取一个数值赋予a
'''
var1=float(random.uniform(-100,100))#在-100到100之间的实数中随机先去一个数值赋予var1
var2=float(random.uniform(-100,100))#在-100到100之间的实数中随机先去一个数值赋予var2
if(var1==var2):#------------------将var1和var2进行比较并返回下列结果
    print("var1等于var2")#---------var1和var2相等
else:
    print("var1不等于var2")#---------var1和var2不想等
#str="1"
#print("在随机数var1中1出现的次数：",var1.count(str))
b=abs(var1)#将a的绝对值赋予b
c=math.ceil(b)#将b的大于他的最近正整数赋予c
d=math.floor(var1)#将a的小于他的最近正整数赋予d
e=math.modf(var1)#将a的值的浮点部分和整数部分分开
print("您输入的值的绝对值是：%f"%b)
print("您输入的值的最近的大于或者等于他的一个整数是:%.3d"%c)
print("您输入的值的最近的小于或者等于他的一个整数是:%.3f"%d)
print("您输入的值的小数部分和整数部分是:",e)
'''
str1="www.google.com"
sub1="w"
print("在字符串str1中w的出现次数是",str1.count(sub1,3,len(str1)))
#print(random.choice([1,2,4,5,7]))
#print(random.choice(range(1,10,2)))
#print(random.random())
list=[4,10,8,20,90,85,63]
#random.shuffle(list)
#print(list)
#name='张三'
#age=28
#sail=258.6479958
#print("我的名字是：%s，我的年龄是%d,我的工资是%.4f"%(name,age,sail))
print(len(a))
index=0
# while index<=