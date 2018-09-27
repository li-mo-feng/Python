import requests
proxy='127.0.0.1:8087'
proxies={
    'http':'http://'+proxy,
    'https':'https://'+proxy,
}
try:
    response=requests.get('https://httpbin.org/get',proxies=proxies,verify=False)
    # 在设置代理的时候直接 添加 proxies和关闭SSL验证即可
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)