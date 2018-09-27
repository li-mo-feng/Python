import requests
res=requests.get("https://ws1.sinaimg.cn/large/006Xzox4ly1fskvg7qafog307s0507tj.gif")
data=res.content
file=open("F://图片//大猩猩.gif","wb")
file.write(data)
file.close()