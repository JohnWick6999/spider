import urllib.request
import urllib.error
url = "https://blog.csdn.net/sulixu/article/details/119818949"
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
    }
try:
    request = urllib.request.Request(url, headers= headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError as e:
    print("系统正在升级。。。")
# 出现URLError一般是主机，端口或者参数出错了
except urllib.error.URLError as x:
    print("我都说了，系统正在升级。。。")