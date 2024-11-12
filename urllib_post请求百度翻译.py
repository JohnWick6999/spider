# post请求
import urllib.request
import urllib.parse
import json
# 请求路径
url = "https://fanyi.baidu.com/sug"
# 请求头
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
# 请求参数
data = {
    "kw":"spider"
}
# 以上三个正好是Request方法需要传入的三个参数。

# post请求的参数一定要进行编码！！！然后需要调用encode方法。
data = urllib.parse.urlencode(data).encode("UTF-8")
# print(data)
# post请求的参数是不会拼接在url后面的，而是要放在Request（请求对象定制）的参数中。
request = urllib.request.Request(url, data, headers)
# print(request)
response = urllib.request.urlopen(request)
# 报错啦！！！(第17行不使用encode的后果)
# 使用Request方法向服务器发送请求时，data形参要接收的值是字节类型，而不是字符串类型！！！
# print(response)

content = response.read().decode("UTF-8")
# 打印的值是Json字符串
# print(type(content))
# print(content)

content_python_dict = json.loads(content)
print(type(content_python_dict))
print(content_python_dict)