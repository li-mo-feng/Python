#!/usr/bin/env python
def fb(n):
    if n ==1 or n ==2:
        res=1
        return res
    else:
        res=fb(n-1)+fb(n-2)
        return res
ss=fb(6)
print(ss)