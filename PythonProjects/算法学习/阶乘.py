# 递归的思想
def s(n):
    if n==0 or n ==1:
        return 1
    else:
        return (n*s(n-1))

a=s(5)
print(a)

# for循环
i=1
n=5
for s in range(1,n+1):
    i=i*s
print(i)

# 