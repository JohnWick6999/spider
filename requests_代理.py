import requests

url = 'https://www.baidu.com/s?wd=ip'

headers = {
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  # "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9",
  "Cache-Control": "max-age=0",
  "Connection": "keep-alive",
  "Cookie": "BIDUPSID=6F46F4EF280ACB26E98DA0904C3DCBFA; PSTM=1736162952; BAIDUID=6F46F4EF280ACB26F9E65ED2B86C7A58:FG=1; BD_UPN=12314753; H_PS_PSSID=60279_61027_60853_61492_61531_61520_61565_61634_61638_61553_61695; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_OTQ5YmIwNmJlNTE4OGU0NTc0MDI3MjA4ZTEzODRhMjQ2NTE4ODZiMWJkN2RmZWEyYTA3YzgzMTUzZDMzZjRjZDcwMWU3ZTMzMTU0MGMzNTkyNWQ4MDljYjE4YmQxN2Y4NGJjOTA3ODA4ZTIzNWNiYWI1NzQ5MTQ2OWNmOGNhYjQ0ZDQwZGY3M2VlZWJhZGM0NDIwZTBmNDNhMDVlMDJhN2JmMTY0NmNhYWJhYTEyNTdjN2M4ZTIwZTRkODA2MTNkYmQwMjhjODQzYzAzYTRiZjVmMTU0ZGMyOGZiMjcyYzk=; BAIDUID_BFESS=6F46F4EF280ACB26F9E65ED2B86C7A58:FG=1; BD_HOME=1; BA_HECTOR=24ak2ka100a4840h840420018vhdi01jnnu6p1v; ZFY=Ijz:Bcj30nu0Tb:ATrK67BWj1Nb6m80v5qbRcbOUYad:Ag:C; BD_CK_SAM=1; PSINO=2; delPer=0; COOKIE_SESSION=16_0_2_2_0_3_1_0_2_2_9_2_0_0_0_0_0_0_1736177391%7C2%230_0_1736177887%7C1%7C1; H_PS_645EC=e526sE%2FUhR16ud5J8WZfrf1UW2%2FYN3Tom1NaWWDdJYVQTy%2FuAEVdBEGTVJI; B64_BOT=1",
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


data = {
    'wd':'ip'
}

proxy = {
  'http': '47.122.65.254:8080'
}
response = requests.get(url, params=data, headers=headers, proxies=proxy)
content = response.text

with open('ip.html', 'w', encoding='utf-8') as f:
    f.write(content)