import requests
from bs4 import BeautifulSoup
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
         'AppleWebKit/537.36 (KHTML, like Gecko)'
         'Chrome/67.0.3396.87 Safari/537.36',
# "Cookie" : "bid=_iuih7V7vQg; __utma=30149280.686616479.1528283558.1530007175.1530171002.3; __utmz=30149280.1530007175.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll=118254; _vwo_uuid_v2=DDAD589422E5FC6D881739228F0894ABC|87d6d26010b09cba0c57497da789c26a; _pk_id.100001.3ac3=d0430b68618c4ecb.1530170998.1.1530172903.1530170998.; _pk_ses.100001.3ac3=*; __utmb=30149280.13.10.1530171002; __utmc=30149280; __utma=81379588.1666877968.1530171002.1530171002.1530171002.1; __utmb=81379588.10.10.1530171002; __utmc=81379588; __utmz=81379588.1530171002.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); viewed=1770782_1041482; gr_user_id=2a9977ee-e45a-42fb-9f57-db3ad671d49a; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=fa8a6938-3da2-407b-9a58-ead79de0774e_true; gr_cs1_fa8a6938-3da2-407b-9a58-ead79de0774e=user_id%3A0; __yadk_uid=XPL5SNrEwcjEiJazOj9mKsdPiIdH7Ldj; ps=y; __utmt=1; dbcl2=180430178:IFN3V8Dn4Ew; ck=p_Mk; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18043; __utmt_douban=1; ap=1"
         }
path="E:/爬虫成果/豆瓣读书250/"
nurl="https://book.douban.com/top250?start="
proxy='127.0.0.1:8087'
proxies={
    'http':'http://'+proxy,
    'https':'https://'+proxy,
}
try:
    response=requests.get('https://httpbin.org/get',proxies=proxies,verify=False)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)
n=0
while n<=99999999:
    url = nurl + str(n)
    response=requests.get(url,headers,proxies=proxies,verify=False)
    # print(response.text)
    soup=BeautifulSoup(response.text,"lxml")
    # print(soup.prettify())
    bnames=soup.select("#content > div > div > div > table > tr > td > div > a")
    # count
    for ss in bnames:
        bname=ss.get_text(strip=True)
        print(bname)
        file = open(path + bname + ".txt", "a+")
        # print(ss.text)
        # file.write()
        file.close()
    n+=25
else:
    print("jieshu")