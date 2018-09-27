from urllib import request
url=r"https://www.jd.com/"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
         'AppleWebKit/537.36 (KHTML, like Gecko)'
         'Chrome/67.0.3396.87 Safari/537.36'}

dabao=request.Request(url,headers=headers)
response=request.urlopen(dabao)
page=response.read().decode('utf-8')
print(page)