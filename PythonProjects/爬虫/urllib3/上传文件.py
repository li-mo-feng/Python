import urllib3
import json
file=open("F:\图片\图片",'rb')
data=file.read()

http=urllib3.PoolManager()
response=http.request('post','https://httpbin.org/post',fields={'filefi'})