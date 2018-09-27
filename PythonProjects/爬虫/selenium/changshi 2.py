from selenium import webdriver
from bs4 import BeautifulSoup
import requests
# client=
# option=webdriver.ChromeOptions()
# option.add_argument("headless")
# 不打开浏览器进行操作
import time
p_url='https://s.taobao.com/'
# 头地址
kw='search?q=ipad'
# 关键字
# for i in range(1,2):
i=0
lnum='&s=%s'%str(44*i)
# 页码的拼接
url=p_url+kw+lnum
browser=webdriver.Chrome()
# browser=webdriver.Chrome(chrome_options=option)
# browser=webdriver.Chrome()
# 这里必须是chrome_option,不能够直接option
browser.get(url)
res=browser.page_source
soup=BeautifulSoup(res,'lxml')
list=soup.select(' div.pic > a')
for i in list:
    surl=i['href']
    url='http:'+surl
    # 一定要详细查看网址内容，这里有的网址已经有了HTTP这个前缀，如果不仔细查看肯定会报错
    print(url)
browser.close()