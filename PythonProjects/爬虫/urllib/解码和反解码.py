from urllib import parse

data=parse.quote("我去立马隔壁",encoding="gbk")
# 将目标字符用XX方式进行编码
print(data)
str=parse.unquote(data,encoding="gbk")
# 将目标字符集用XXX方式进行反编码
print(str)