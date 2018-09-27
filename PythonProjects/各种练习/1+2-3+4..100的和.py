def run(x):
    list=[]
    for i in range(1,x):
        if i%2==0:
            a=-i
            list.append(a)
        elif i%2!=0:
            b=i
            list.append(b)
    a = sum(list)
    print(a)


run(100)