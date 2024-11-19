import urllib.request
from bs4 import BeautifulSoup as bs
url = "https://www.starbucks.com.cn/"
response = urllib.request.urlopen(url)
content = response.read().decode("utf-8")

soup = bs(content, "lxml")
# xpath路径：//ul[@class="grid padded-3 product"]//strong/text()
name_list = soup.select("ul[class='grid padded-3 product'] strong")
for name in name_list:
    print(name.get_text())