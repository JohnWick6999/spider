# 通过登录  然后进入到主界面

# 登录时需要的参数很多
# __VIEWSTATE: cVuhZxMDD5cadqwqwAjTw8FJdvGlNXzREJROgnkn6PEG5HL/oBRkvuPXz6j6xsJYt9moahqTcJC04dN2L3IykbQ+L3NDjuXdUEQzl4F2fD3+0rsTEdT1j2Tnm/paEV4USikuoec0nBlIjX6ycxZ/gUb6u9w=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://www.gushiwen.cn/user/collect.aspx
# email: 2418804495@qq.com
# pwd: abcddef
# code: sn3h
# denglu: 登录

# __VIEWSTATE，__VIEWSTATEGENERATOR，code 它们三个是可变的量。
# __VIEWSTATE，__VIEWSTATEGENERATOR 看不到的数据，一般在页面的源码中。
# 可以看出 __VIEWSTATE，__VIEWSTATEGENERATOR 这两个量在页面源码的隐藏域“hidden”中，所以要获取页面的源码，把它们解析出来。

import requests
from bs4 import BeautifulSoup
import urllib.request as req

# 登陆页面的url地址
url = 'https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx'

headers = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

# 获取页面的源码
response = requests.get(url, headers=headers)
content = response.text

# 解析页面源码，然后获取 __VIEWSTATE，__VIEWSTATEGENERATOR
soup = BeautifulSoup(content, 'lxml')

# 获取 __VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')

# 获取 __VIEWSTATEGENERATOR
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')


# 接下来考虑验证码的问题
# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://www.gushiwen.cn' + code

# 下载验证码图片
# req.urlretrieve(code_url, 'code.jpg')
# requests中有一个方法叫做session，通过session的返回值，使请求变成一个对象。
session = requests.session()

# 验证码url的内容
response_code = session.get(code_url)
# 需要获取二进制数据，因为图片的下载需要二进制。
content_code = response_code.content

with open('code.jpg', 'wb') as f:   # 将二进制数据写入到文件
  f.write(content_code)

# 验证码的图片下载到本地，控制台输入图片中的验证码，将值传给code，就可以登陆。
code_name = input('请输入你的验证码：')

# 点击登录
url_post = 'https://www.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fwww.gushiwen.cn%2fuser%2fcollect.aspx'

# 在"from","email"处填入正确的值
data_post = {
  "__VIEWSTATE": viewstate,
  "__VIEWSTATEGENERATOR": viewstategenerator,
  "from": "http://www.gushiwen.cn/user/collect.aspx",
  "email": "2418804495@qq.com",
  "pwd": "Sbw050826",
  "code": code_name,
  "denglu": "登录"
}
response_post = session.post(url_post, data=data_post, headers=headers)   # 同步前面的session对象
content_post = response_post.text
with open('gushiwen.html', 'w', encoding='utf-8') as f:
  f.write(content_post)