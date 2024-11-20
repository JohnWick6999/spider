from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium import webdriver

path = "msedgedriver.exe"
service = Service(path)
browser = webdriver.Edge(service= service)

url = "https://baidu.com"
browser.get(url)

# 元素定位
# find_element返回一个元素，find_elements返回一个列表

# 根据id找到对象
button = browser.find_element(By.ID, value="su")
print(button)

# 根据标签的属性值获取对象
button = browser.find_element(By.NAME, value="wd")
print(button)

# 根据xpath语句获取对象
button = browser.find_element(By.XPATH, value="//input[@id='su']")
print(button)

# 根据标签的名字获取对象
button = browser.find_element(By.TAG_NAME, value="input")
print(button)

# 使用bs4的语法来获取对象
button = browser.find_element(By.CSS_SELECTOR, value="#su")
print(button)

# 获取页面中的超链接
button = browser.find_element(By.LINK_TEXT, value= "新闻")
print(button)
input()