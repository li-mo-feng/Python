import requests
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
         'AppleWebKit/537.36 (KHTML, like Gecko)'
         'Chrome/67.0.3396.87 Safari/537.36'}
url="https://www.baidu.com"

res=requests.get("https://www.baidu.com/s?wd=tara",headers=headers)
# requests.get("url",data={})
print(res.content.decode("utf-8"))