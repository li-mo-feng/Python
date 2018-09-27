from bs4 import BeautifulSoup
import requests
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
         'AppleWebKit/537.36 (KHTML, like Gecko)'
         'Chrome/67.0.3396.87 Safari/537.36'}

url="http://bj.xiaozhu.com/"

response=requests.get(url,headers=headers)

soup=BeautifulSoup(response.text,"lxml")
print(soup)