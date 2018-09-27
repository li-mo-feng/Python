# 后面一个数是前面两个数之和,要求输出10个数
# def shu(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return shu(n-1)+shu(n-2)
# a=shu(10)
# print(a)




a,b=0,1
while b:
    print(b)
    a,b=b,a+b