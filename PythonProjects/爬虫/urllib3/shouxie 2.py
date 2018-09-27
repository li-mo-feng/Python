import urllib3
import json
data={"woshishuaige ":"hahahah"}
# 先将要上传的内容书写为字典
jdata=json.dumps(data).encode()
# 然后字典转化为json格式

http=urllib3.PoolManager()
response=http.request(
    "post",
    "http://httpbin.org/post",
    body=jdata,
    headers={'Content-Type':'application/json'}
)
str=response.data.decode()

dic=eval(str)
# 字符串转换为字典
print(dic['json'])
# 打印字典内key是json的项