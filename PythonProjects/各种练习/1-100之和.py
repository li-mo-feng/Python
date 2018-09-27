
# print (sum(range(1,101)))
def sun(a):
    n=0
    for i in range(a+1):
        n=i+n
        if i==100:
            print(n)

sun(100)