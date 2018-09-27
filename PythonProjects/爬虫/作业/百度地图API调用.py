import requests
from bs4 import BeautifulSoup
proxy='127.0.0.1:1080'
proxies={
    'http':'http://'+proxy,
    'https':'https://'+proxy,
}
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
         'AppleWebKit/537.36 (KHTML, like Gecko)'
         'Chrome/67.0.3396.87 Safari/537.36'}
url="https://www.qiushibaike.com/"
res=requests.get(url,headers=headers,proxies=proxies)
soup=BeautifulSoup(res.content,"lxml")
authors=soup.select("#qiushi > div > a")
print(authors)
