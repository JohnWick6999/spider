import urllib.request

url = "http://www.baidu.com"

response = urllib.request.urlopen(url)

#类型为 <class 'http.client.HTTPResponse'>
# print(type(response))

#按字节读
# content = response.read(5)
# print(content)

#按行读
# content = response.readline()
# print(content)

#读所有行，一行一行的读，直至读完
# content = response.readlines()
# print(content)

#返回状态码 200：逻辑没有错误
# print(response.getcode())

#获取url地址(返回的值)
# print(response.geturl())

#获取状态信息
# print(response.getheaders())

#一个类型   HTTPResponse
#六个方法   read(),readline(),readlines(),getcode(),geturl(),getheaders()