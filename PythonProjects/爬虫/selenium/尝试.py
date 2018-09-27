from selenium import webdriver
from bs4 import BeautifulSoup
url='https://item.taobao.com/item.htm?id=567144656257&ns=1&abbucket=0#detail'
# url1='https://detail.tmall.com/item.htm?spm=a230r.1.14.6.27cf5268wCIrLC&id=566940629944'
option=webdriver.ChromeOptions()
option.add_argument("headless")
browser=webdriver.Chrome(chrome_options=option)
browser.get(url)
soup=BeautifulSoup(browser.page_source,'lxml')
title = soup.select('#J_Title > h3')[0]['data-title']
print(title)
# title1=soup.select('#J_DetailMeta > div > div > div > div > h1 > a')[0].string
# items = soup.select('em')
# items=soup.select('#J_PromoPrice > dd > div > span')

# for item in items:
#     price='￥'+item.string
#     print(price)
# print(item[0][])


# renqi=item[1]
# price=item[2:4]
# item_num=item[6]
# item_sold=item[7]
# print('renqi:',renqi)
# print('price:',price)
# print('库存数量:',item_num)
# print('销售数量:',item_sold)
#J_PromoPriceNum
browser.close()
