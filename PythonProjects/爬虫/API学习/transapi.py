import requests
import hashlib
import random
def trans():
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
             'AppleWebKit/537.36 (KHTML, like Gecko)'
             'Chrome/67.0.3396.87 Safari/537.36'}
    q=input("请输入要翻译的内容")
    appid="20151113000005349"
    secretKey = 'osubCEzlGjzvw8qdQc41'
    salt = random.randint(32768, 65536)
    sign=appid+q+str(salt)+secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()

    url="http://api.fanyi.baidu.com/api/trans/vip/translate"
    data={'q':q,'from':'zh','to':'en','appid':appid,'salt':salt,'sign':sign}
    response=requests.post(url,headers=headers,data=data)
    ans=response.json()['trans_result'][0]['dst']

    return ans,q
