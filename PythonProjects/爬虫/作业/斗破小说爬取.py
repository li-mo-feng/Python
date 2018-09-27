import requests
from bs4 import BeautifulSoup
path="E:/爬虫成果/斗破苍穹小说/"
url="http://www.doupoxs.com/doupocangqiong/"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
         'AppleWebKit/537.36 (KHTML, like Gecko)'
         'Chrome/67.0.3396.87 Safari/537.36'}

response=requests.get(url,headers=headers)
# print(response.encoding)
# 显示编码信息（ios-8859-1）
# print(response.content.decode("utf-8"))
# 编码显示
soup=BeautifulSoup(response.content,"lxml")
# response只是一个页面对象
# print(soup)
# 美化显示
zhangjies=soup.select("body > div > div > ul > li > a")
# 所有的章节
file = open(path + "斗破苍穹" + ".txt", "a+")
for zhangjie in zhangjies:
    # 遍历的单个章节
    zurls=zhangjie["href"]
    # 单个章节的地址
    murl="http://www.doupoxs.com"+zurls
    # 单个章节的完整地址
    html=requests.get(murl)
    # 获取单个章节的信息
    data=BeautifulSoup(html.content,"lxml")
    # 获取章节内容
    neirongs=data.select("body > div > div > div > div > p")
    # 选择里面的P标签
    for ps in neirongs:
        for i in ps:
            file.write(str(i))
    file.write("\n")
file.close()
