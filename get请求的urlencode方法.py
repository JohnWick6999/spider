#当有多个应用参数的时候，使用urlencode方法就更加方便了。
#urlencode方法与quote方法同属于urllib.parse
import urllib.parse
import urllib.request

url = 'https://www.baidu.com/s?wd=周杰伦&sex=男'

#urlencode方法要求里面的参数以字典的形式存在！！！
#它会将字典中的键值对用“&”拼接在一起，键和值之间用“=”连接。
# data = {
#     "wd" : "周杰伦",
#     "sex" : "男"
# }
# a = urllib.parse.urlencode(data)
# print(a)

#https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&location=%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE%E7%9C%81
#获取以上网址的网页源码

base_url = "https://www.baidu.com/s?"
data = {
    "wd":"周杰伦",
    "sex":"男",
    "location":"中国台湾省"
}
data = urllib.parse.urlencode(data)
#拼接成正确的资源路径（url）
new_data = base_url + data
#避免UA反爬
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
request = urllib.request.Request(new_data,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("UTF-8")
print(content)