from urllib import request,error
try:
    request.urlopen(r"https://www.sadasdadasdada.com")
except error.URLError as e:
    print(e.reason,sep="\n")