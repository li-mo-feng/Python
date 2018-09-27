import requests
res=requests.get("https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo-transcode/1767502_56ec685f9c7ec542eeaf6eac93a65dc7_6fe25cd1347c_3.mp4",
             stream=True)
file=open("F://图片//1.mp4","wb")
for line in res.iter_content():
    file.write(line)

file.close()