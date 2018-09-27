from urllib import request,error
try:
    request.urlopen(r"https://cuiqingcai.com/index.htm")
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep="\n")

