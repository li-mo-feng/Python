# def num(a,n):
#     #N是每个人前一个大几岁,a是有多少个人
#     s=10#最前面那个人是10岁
#     for i in range(a-1):#有多少个人比最前面那个人大
#         s+=n
#         while i==a:
#             print()
#     print("第%d个人的岁数是%d"%(a,s))
# num(5,2)
#
#
#
#
# 又五个人,第五个是10,每个人比前一个大2岁
def age(n):
    if n==1:#出口是第一个人是10岁
        ages=10
        return ages

    # 因为是自己调用自己所以需要返回age的值.
    else:
        ages=(n-1)+2
        return ages
    #递归,需要自己调用自己直到满足出口条件.