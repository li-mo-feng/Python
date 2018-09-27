num=input("请输入一个数")
if list(num)[::1]==list(num)[::-1]:
    print("改数字是%d为回文数"%(int(num)))
else:
    print("bushi ")

