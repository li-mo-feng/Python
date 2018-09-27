a=int(input("请先输入任意整数a"))#同时进行数据类型转换
b=int(input("请再输入任意整数b"))#同上
#a=int(a)
#input输入的值都是str型，然而计算无法使用
#TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
#b=int(b)
#字符型转换-理由同上
c=str(pow(a,b))
print("a的b次方的值是：",c)
