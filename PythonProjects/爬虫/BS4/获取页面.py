from bs4 import BeautifulSoup
import requests
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
         'AppleWebKit/537.36 (KHTML, like Gecko)'
         'Chrome/67.0.3396.87 Safari/537.36'}
path="F:/图片/斗图3/"
url="https://www.52doutu.cn/pic/"
res=requests.get(url,headers)
soup=BeautifulSoup(res.text,"html.parser")
# print(soup)
imgs=soup.find_all("img",class_="lazyload")
a=soup.select(" div > div > a > div > img ")
print(a)
count=1
# for img in imgs:
#
#
#     ss=img["data-original"]
#
#
#     res=requests.get(ss)
#     file=open(path+str(count)+ss[-4:],"wb")
#     file.write(res.content)
#     file.close()
#     count+=1