import urllib3
import json
http=urllib3.PoolManager()
response=http.request("get","https://httpbin.org/ip",)
res=json.loads(response.data.decode())
print(res)