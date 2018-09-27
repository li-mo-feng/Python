# 求1+。。+n的值
def ss(n):
    if n==1:
        return 1
    else:
        return ss(n-1)+n

#
# a=ss(10)
# print(a)

def year(n):
    if n==1:
        return 10
    else:
        return year(n-1)+2


m=year(5)
print(m)