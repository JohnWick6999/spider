import urllib.request
from lxml import etree
url = "https://www.baidu.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("UTF-8")
# print(content)

# 解析网页源码，获取想要的数据。
tree = etree.HTML(content)
# xpath的返回类型是列表，通过列表下标访问特定元素
result = tree.xpath("//input[@id='su']/@value")[0]
print(result)