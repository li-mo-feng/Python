import urllib3
url=r"https://www.jd.com/"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
         'AppleWebKit/537.36 (KHTML, like Gecko)'
         'Chrome/67.0.3396.87 Safari/537.36'}

http=urllib3.PoolManager()
response=http.request(
    "post",
    "http://httpbin.org/post",
    fields={"1801":"zhangsan"},
    headers=headers
)
print(response.data.decode())