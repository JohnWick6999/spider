import requests
import json

# 抓取数据建议使用英文输入法，要不然找不到sug
url = 'https://fanyi.baidu.com/sug'

headers = {
  "Accept": "*/*",
  # "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9",
  "Connection": "keep-alive",
  "Content-Length": "6",
  "Content-Type": "application/x-www-form-urlencoded",
  "Cookie": "BIDUPSID=6F46F4EF280ACB26E98DA0904C3DCBFA; PSTM=1736162952; BAIDUID=6F46F4EF280ACB26F9E65ED2B86C7A58:FG=1; H_PS_PSSID=60279_61027_60853_61492_61531_61520_61565_61634_61638_61553_61695; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=6F46F4EF280ACB26F9E65ED2B86C7A58:FG=1; delPer=0; PSINO=2; BA_HECTOR=25040lak2hah2la0al84a00kbinm4b1jnnrds1u; ZFY=Ijz:Bcj30nu0Tb:ATrK67BWj1Nb6m80v5qbRcbOUYad:Ag:C; ab_sr=1.0.1_OTQ5YmIwNmJlNTE4OGU0NTc0MDI3MjA4ZTEzODRhMjQ2NTE4ODZiMWJkN2RmZWEyYTA3YzgzMTUzZDMzZjRjZDcwMWU3ZTMzMTU0MGMzNTkyNWQ4MDljYjE4YmQxN2Y4NGJjOTA3ODA4ZTIzNWNiYWI1NzQ5MTQ2OWNmOGNhYjQ0ZDQwZGY3M2VlZWJhZGM0NDIwZTBmNDNhMDVlMDJhN2JmMTY0NmNhYWJhYTEyNTdjN2M4ZTIwZTRkODA2MTNkYmQwMjhjODQzYzAzYTRiZjVmMTU0ZGMyOGZiMjcyYzk=; RT=\"z=1&dm=baidu.com&si=131fd90b-cd20-452a-a068-9c6d1fab653f&ss=m5l6ccol&sl=5&tt=2gw&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1hvz\"",
  "DNT": "1",
  "Host": "fanyi.baidu.com",
  "Origin": "https://fanyi.baidu.com",
  "Referer": "https://fanyi.baidu.com/mtpe-individual/multimodal?ext_channel=Aldtype",
  "Sec-Ch-Ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

data = {
    'kw':'eye'
}

# url:请求地址 data:请求参数 kwargs:字典
response = requests.post(url, data=data, headers=headers)
content = response.text
obj = json.loads(content)
print(obj)

# post请求不需要编解码;它区别于get请求的params,使用的是data;并且不需要请求对象的定制。