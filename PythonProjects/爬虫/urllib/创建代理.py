import urllib.request


proxy_support = urllib.request.ProxyHandler({'socks5': '127.0.0.1:1080'})
# 设置代理
opener = urllib.request.build_opener(proxy_support)
# 创建代理
urllib.request.install_opener(opener)
# 启用代理
a = urllib.request.urlopen("https://cn.bing.com").read().decode("utf8")
print(a)
