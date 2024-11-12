#quote方法将一个词变成Unicode编码的形式，一次只能转一个输入的单词或语句。
import urllib.request
import urllib.parse
url = 'https://www.baidu.com/s?wd='

headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
#将周杰伦三个字变成Unicode编码的格式
#urllib.parse.quote()
name = urllib.parse.quote("周杰伦")
# print(name)
url = url + name
# print(url)

request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("UTF-8")
print(content)