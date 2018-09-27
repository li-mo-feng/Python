import requests
import urllib3
from bs4 import BeautifulSoup

path="E:/爬虫成果/都市小说/"
url="https://www.38660.com/book/0/26138/"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
         'AppleWebKit/537.36 (KHTML, like Gecko)'
         'Chrome/67.0.3396.87 Safari/537.36'}

response=requests.get(url,headers)
soup=BeautifulSoup(response.content,'lxml')
links=soup.select('#main > div > div > ul > li > a')
# print(links)
for link in links:
    title=link.text
    page=link['href']
    response2=requests.get(link['href'])
    soup2=BeautifulSoup(response2.content,'lxml')

    zhengwen=soup2.select('#htmlContent')
    for i in zhengwen:
        ss=i.text.replace('download depiler from: （结尾英文忽略即可）</div>', '')
        file=open(path+'都市沉浮'+'.txt','a+',encoding='utf-8')
        file.write(title)
        file.write('\n')
        file.write(ss)
        file.close()