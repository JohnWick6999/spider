import random
import urllib.request

proxies_pool = [
{
    "http":"218.87.205.201:16146"
},
{
    "http":"218.87.205.201:16146"
}
]
proxies = random.choice(proxies_pool)
url = "http://www.baidu.com/s?wd=ip"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
request = urllib.request.Request(url, headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
with open("daili_ip.html", "w", encoding= "utf-8")as f:
    f.write(content)