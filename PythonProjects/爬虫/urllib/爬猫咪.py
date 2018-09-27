from urllib import request
import re
import os
path=r"F:\图片\猫咪"
response=request.urlopen(r"http://www.maomijiaoyi.com/")
html=response.read().decode("utf-8")
imgs=re.findall(r'attached[^s]*?jpg',html)
count=1
for img in imgs:
    url=os.path.join("http://www.maomijiaoyi.com/",img)
    data=request.urlopen(url).read()
    file=open(path+"\\"+str(count)+".jpg","wb")
    file.write(data)
    file.close()
    count+=1