a=0
b=0
for i in range(2,101):
    if i % 2==0:
        # 偶数之和
        a+=i
    else:
        b+=-i
#         奇数之和
print(a+b)