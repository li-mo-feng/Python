import requests
from bs4 import BeautifulSoup
path="E:/爬虫成果/斗破苍穹小说/"
murl="http://www.doupoxs.com"
url="http://www.doupoxs.com/doupocangqiong/"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
         'AppleWebKit/537.36 (KHTML, like Gecko)'
         'Chrome/67.0.3396.87 Safari/537.36'}
response=requests.get(url,headers)
soup=BeautifulSoup(response.content,"lxml")
plists=soup.select("body > div > div > ul > li > a")
# 每一个章节的链接
for plist in plists:
    # 章节对象
    pname= open(path + plist.text + ".txt", "a+")
    # 单张的文件名
    purl=murl+plist["href"]
    # 单章节实际地址
    pdata=requests.get(purl)
    # 访问页面
    psoup=BeautifulSoup(pdata.content,"lxml")
    # BS4读取
    mps=psoup.select("body > div > div > div > div > p")
    # print(mps)
    # 获取页面所有的P标签
    for p in mps:
        pmain=p.text
        pname.write(pmain)
        pname.write("\n")
    pname.close()
        # 单章节的文件名
        # pname.write(p.text)
        # pname.close()
