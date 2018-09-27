import urllib3
import  requests
requests.packages.urllib3.disable_warnings()
# 去掉SSl警告

http=urllib3.PoolManager()
response=http.request("get","https://www.baidu.com")
res=response.data.decode("utf-8")

print(res)