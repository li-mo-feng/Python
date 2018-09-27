from selenium import webdriver
from pyquery import PyQuery as pq
from multiprocessing import Process
from bs4 import BeautifulSoup
import  requests
from threading import Thread

option = webdriver.ChromeOptions()
option.add_argument("headless")


def ipget():
    browser = webdriver.Chrome(chrome_options=option)
    url='http://www.xicidaili.com/nn/'
    browser.get(url)
    source=browser.page_source
    doc=pq(source)
    items=doc('.odd').items()
    list=[]
    # 1.先获取页面上的IP地址
    for item in items:
        a=item.text().split('\n')
        ip=a[0]
        port=a[1]
        ip_tuple=(ip,port)
        list.append(ip_tuple)
    iplist=dict(list)
    # 获取到的是验证可用后的IP和端口组成的字典
    browser.close()
    return iplist


# ip验证
def ip_yanzheng():
    iplist=ipget()
    goodip=[]
    for ip in iplist:
        option.add_argument('--proxy-server=http://' + ip)
        browser=webdriver.Chrome(chrome_options=option)
        url_yanzheng = 'http://ip.chinaz.com/getip.aspx'
        browser.get(url_yanzheng)
        p=browser.find_element_by_css_selector('body').text
        if p == '' or 'ip' not in p:
            pass
        else:
            goodip.append(p)
    return goodip