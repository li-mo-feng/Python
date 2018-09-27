import requests
data={"123":"456"}
res=requests.post("https://httpbin.org/post",data)
print(res.json()["form"])