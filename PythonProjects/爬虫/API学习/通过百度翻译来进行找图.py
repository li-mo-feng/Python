import requests
from bs4 import BeautifulSoup
from transapi import *
from pyquery import PyQuery
ansq=trans()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         'AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/67.0.3396.87 Safari/537.36'}
surl='https://www.pexels.com/search/'
# 不带搜索内容的地址
q=ansq[0]
# 接收翻译过来的结果
url=surl+q+'/'
# 网址拼合
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,'lxml')
imgs=soup.select('body > div > div > div > article > a > img')
# 获取所有的img地址

for img in imgs:
    print(img['src'])