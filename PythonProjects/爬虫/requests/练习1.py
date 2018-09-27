import requests
import re
for i in range(1,11):
    url="https://www.52doutu.cn/pic/"
    response=requests.get(url+str(i))
    html=response.text
    imgs=re.findall(r'https://www.52doutu.cn/static/images/upload/[^\s]*.jpg',response.text)
    count=1
    for img in imgs:
        # print(img)
        res=requests.get(img)
        data=res.content
        file=open("F://图片//图片//"+str(count)+".jpg","wb")
        file.write(data)
        file.close()
        count+=1
    # print(response.encoding)
    # print(html)
    # print(response.json())