# 求1+。。+n的值
def ss(n):
    if n==1:
        return 1
    else:
        return ss(n-1)+n

#
# a=ss(10)
# print(a)


