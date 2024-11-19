# 模拟浏览器不能在获得的源码中看到其中一些内容，比如当前案例中京东的秒杀页面。
import urllib.request

url = "https://www.jd.com/"

response = urllib.request.urlopen(url)
content = response.read().decode("utf-8")
print(content)