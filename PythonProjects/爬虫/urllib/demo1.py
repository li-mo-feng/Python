from urllib import request
import re
url=r"https://alpha.wallhaven.cc/search?q=%22anime+girls%22&page=28"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
         'AppleWebKit/537.36 (KHTML, like Gecko)'
         'Chrome/67.0.3396.87 Safari/537.36'}
# 头和源地址
dabao=request.Request(url,headers=headers)
# 包含头的打包地址
response=request.urlopen(dabao)
#访问打包好的地址
html=response.read().decode('utf-8')
# 读取地址的源代码
path="F:\图片\猫咪"
# 存放原始路径
imgs=re.findall(r'https://alpha.wallhaven.cc/wallpapers/thumb/small/th-\d{6}.jpg',html)
# 在打包代码中匹配数据
print(imgs)
count=1
for img in imgs:
    data=request.urlopen(img).read()
    file=open(path+"\\"+str(count)+".jpg","wb")
    # 存放文件的路径组合
    file.write(data)
    file.close()
    count+=1
