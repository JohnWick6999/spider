from selenium.webdriver.edge.service import Service
from selenium import webdriver

path = "msedgedriver.exe"
service = Service(path)
browser = webdriver.Edge(service= service)

url = "https://www.jingdong.com"
browser.get(url)
content = browser.page_source
print(content)
input()