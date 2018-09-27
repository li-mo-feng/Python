import  requests
res=requests.get("http://www.autohome.com/news")
res.encoding="gbk"
print(res.text)