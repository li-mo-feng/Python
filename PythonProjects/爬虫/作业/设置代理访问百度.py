import requests
url=r"https://www.jd.com/"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
         'AppleWebKit/537.36 (KHTML, like Gecko)'
         'Chrome/67.0.3396.87 Safari/537.36'}
proxy="127.0.0.1:1080"
proxies={
    'http':proxy,
    'https':proxy,
}
response=requests.get(url,headers=headers,proxies=proxies,verify=False)
print(response.text)