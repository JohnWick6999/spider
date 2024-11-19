# 1.导入selenium
from selenium import webdriver
from selenium.webdriver.edge.service import Service

# 2.创建浏览器操作对象
path = 'msedgedriver.exe'
service = Service(executable_path=path)
browser = webdriver.Edge(service=service)

# 3.访问网站
url = "https://www.jingdong.com"
browser.get(url)

# page_source获取网页源码
content = browser.page_source
print(content)

input()
