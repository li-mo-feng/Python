from urllib import request
import re
import os

path="F:\图片\斗图2"
count=1
for i in range(1,100):
    #
    url= "https://www.52doutu.cn/pic/"
    urls=url+str(i)
    #关于循环遍历

    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
             'AppleWebKit/537.36 (KHTML, like Gecko)'
             'Chrome/67.0.3396.87 Safari/537.36'}
    dabao=request.Request(urls,headers=headers)
    response=request.urlopen(dabao).read().decode("utf-8")
    # print(response)
    imgs=re.findall(r'https://www.52doutu.cn/static/images/upload/[^\s]*.jpg',response)
    print(len(imgs))
    for img in imgs:
        print(img)
    for i in imgs:
        data=request.urlopen(i).read()
        file=open(path+"\\"+str(count)+".jpg","wb")
        file.write(data)
        file.close()
        count+=1