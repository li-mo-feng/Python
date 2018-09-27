a=10
b=10
c=[1,2,3,4,5]
d=[1,2,3,4,5]
print(a is b)
print(a==b)
# is比较的是内存的数值是否相等
print(c is d)
print(c==d)
# ==比较的是数值上的相等
e='abc'
f='abc'
print(e is f )
# 因为只是单纯一层比较所以相等
print(e==f)
# 多层比较比如列表，字典等多层比较内存就不一样，但是数值可能一样