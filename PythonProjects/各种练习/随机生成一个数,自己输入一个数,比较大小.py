import random
a=random.choice(range(0,100))
b=int(input("请输入一个0到100内的整数"))
if a<b:
    print("您输入的数值是%d,随机生成的数值是%d,更大的是随机数%d"%(b,a,a))
else:
     print("您输入的数值是%d,随机生成的数值是%d,更大的是您输入的数值%d"%(b,a,b))


