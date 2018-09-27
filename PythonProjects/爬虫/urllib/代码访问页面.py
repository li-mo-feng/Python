from urllib import request
url2="https://www.jd.com/"
response=request.urlopen(url2)
page=response.read().decode("utf-8")
print(page)