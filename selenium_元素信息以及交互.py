from selenium import webdriver


path = 'C:/msedgedriver.exe'

browser = webdriver.Edge(path)

url = 'https://www.baidu.com'
browser.get(url)
get = browser.find_element_by_id('su')

# 获取标签的属性
print(get.get_attribute('class'))
# 获取标签的名字
print(get.tag_name)

# 获取的是两个尖括号之间的内容(元素文本)
a = browser.find_element_by_link_text('新闻')
print(a.text)
