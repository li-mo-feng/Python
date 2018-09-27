# 第五个人10岁，面一个分别比后面一个大2岁，求第N个人多少岁
def age(n):
    if n == 5:
        ages=10
        return ages
    else:
        ages=age(n+1)+2
        return ages

ss=age(4)
print(ss)
