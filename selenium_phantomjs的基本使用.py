from selenium import webdriver
from time import sleep

path = 'phantomjs.exe'
browser = webdriver.PhantomJS(path)
url = 'https://www.baidu.com'
browser.get(url)
browser.save_screenshot('baidu.png')
sleep(2)

get = browser.find_element_by_id('kw')
get.send_keys('昆凌')
sleep(3)
browser.save_screenshot('昆凌.png')