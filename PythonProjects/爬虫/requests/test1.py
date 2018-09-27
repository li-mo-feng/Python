import requests
response=requests.get("https://www.baidu.com")
print(response)
response2=requests.post("https://httpbin.org/post",data={"123":"456"})
print(response2.json())

