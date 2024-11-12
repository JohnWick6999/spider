#使用urllib来获取百度首页的源码。
import urllib.request

#1.定义一个url（要访问的地址）
url = "http://www.baidu.com"

#2.模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

#3.获取响应中的页面的源码
#将read方法返回的二进制数据转换为字符串（解码）decode("编码的形式")
content = response.read().decode("UTF-8")

#4.打印数据
print(content)