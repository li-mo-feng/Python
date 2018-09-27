import requests
proxy='127.0.0.1:8087'
proxies={
    'http':'http://'+proxy,
    'https':'https://'+proxy,
}
try:
    response=requests.get('https://httpbin.org/get',proxies=proxies)
    # 在设置代理的时候直接 添加 proxies不用设置证书！

    # 下面的代码仅仅用于测试
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)