#!/usr/bin/env python
list=[1,2,3,4,5]
list2=[]
list3=[]
for i in list:
    if i % 2==0:
        list2.append(i)
    else:
        list3.append(i)
ss=dict(zip(list2,list3))
print(ss)