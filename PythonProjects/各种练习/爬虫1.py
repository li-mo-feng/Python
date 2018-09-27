from urllib import request
import urllib.request
url=r"http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%9B%BE%E7%89%87"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
         'AppleWebKit/537.36 (KHTML, like Gecko)'
         'Chrome/67.0.3396.87 Safari/537.36'}

dizhi=request.Request(url,headers=headers)
proxy_support=urllib.request.ProxyHandler({'sock5':'127.0.0.1:8888'})

opener=urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)


a=urllib.request.urlopen(url).read().decode('utf-8')
print(a)