import requests

headers = {
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  # "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9",
  "Cache-Control": "max-age=0",
  "Connection": "keep-alive",
  "Cookie": "BIDUPSID=6F46F4EF280ACB26E98DA0904C3DCBFA; PSTM=1736162952; BAIDUID=6F46F4EF280ACB26F9E65ED2B86C7A58:FG=1; BD_UPN=12314753; BA_HECTOR=a501al808ga42ha0048l018g0vbikn1jnnfkf1u; BAIDUID_BFESS=6F46F4EF280ACB26F9E65ED2B86C7A58:FG=1; ZFY=Ijz:Bcj30nu0Tb:ATrK67BWj1Nb6m80v5qbRcbOUYad:Ag:C; H_PS_PSSID=60279_61027_60853_61492_61531_61520_61565_61634_61638_61553_61695; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; baikeVisitId=e3849e35-180b-47b1-8723-f5fb87a37073; BD_HOME=1",
  "DNT": "1",
  "Host": "www.baidu.com",
  "Sec-Ch-Ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "none",
  "Sec-Fetch-User": "?1",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}


url = 'https://www.baidu.com'
response = requests.get(url, headers=headers) # 使用请求标头来获取完整的网页源码

# 一个类型和六个属性
print(type(response)) # Response类型
response.encoding = 'utf-8' # 设置响应的编码格式
print(response.text) # 以字符串的形式返回页面的源码
print(response.url) # 返回一个url地址
print(response.content) # 返回二进制的数据
print(response.status_code) # 返回相应的状态码
print(response.headers) # 返回响应头