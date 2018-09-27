a=1
try:
    print("第一步")
    # 肯定会进入的操作
    a+=1
except:
    # 遇到报错才会进入的操作
    print("第二步")
    a+=1
else:
    # 没有报错会执行
    print("第三步")
    a+=1
finally:
    # 肯定会执行
    print("第四步")
    a+=1
    print(a)