from selenium import webdriver
from bs4 import BeautifulSoup
import requests
option=webdriver.ChromeOptions()
option.add_argument("headless")
browser=webdriver.Chrome(chrome_options=option)
p_url='https://s.taobao.com/'
kw='search?q=ipad'
url=p_url+kw
browser.get(url)
source=browser.page_source
soup=BeautifulSoup(source,'lxml')
items=soup.select('div > div > div > div.pic > a')
tag_imgs=soup.select('div > div > div > div.pic > a > img')
i=0
for item2 in items:
    for item1 in tag_imgs:
        href = item2['data-href']
        title=item1['alt']
        if 'https' in href:
            res=requests.get(href).text
        #    获取到的所有商品的页面的源代码
            soup2=BeautifulSoup(res,'lxml').text
            print(soup2)
            # if '天猫' in soup2:
            #     print("heiheihei")
            # else:
            #     print('我是淘宝')

                # soup2.select('#J_PromoPrice > dd > div > span')
browser.close()