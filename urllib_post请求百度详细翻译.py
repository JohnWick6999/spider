import urllib.request
import urllib.parse
import json
url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
headers = {
  "Accept": "*/*",
  # "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9",
  "Connection": "keep-alive",
  "Content-Length": "7",
  "Content-Type": "application/x-www-form-urlencoded",
  "Cookie": "BAIDUID=F6C7C7F9DDCC41C11B3C3EDEBC96AD0C:FG=1; BAIDUID_BFESS=F6C7C7F9DDCC41C11B3C3EDEBC96AD0C:FG=1; ab_sr=1.0.1_MDM0MTJlY2UxZDU4NzA5Nzg0YmEzOGU1MmU1MTRhZmUwMWZkZDgzOWZiNmMzYmZmYzNlMTIwNTliZTFkMjg2MjgzZjM2ZGYxYWNjMjYwZGY5OWQ0MmQ3NWNmODJkOTRiYzc1YjU4NGQ0MzJkZDQ0OTc0ZjkzZmU2MGI1NzU1MjEzODEyYzdkZjhlOWE5NDFhYTJmMWQzOGRhZThiMGRiNA==; RT=\"z=1&dm=baidu.com&si=26dde009-1d85-4511-a42f-a1f9a3e75668&ss=m304suai&sl=1&tt=2r6&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=3jb\"",
  "Host": "fanyi.baidu.com",
  "Origin": "https://fanyi.baidu.com",
  "Referer": "https://fanyi.baidu.com/mtpe-individual/multimodal?query=lov&lang=srp2zh",
  "Sec-Ch-Ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

data = {
  "from": "en",
  "to": "zh",
  "query": "love",
  "transtype": "realtime",
  "simple_means_flag": "3",
  "sign": "198772.518981",
  "token": "5483bfa652979b41f9c90d91f3de875d",
  "domain": "common"
}

data = urllib.parse.urlencode(data).encode("utf-8")
request = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
content_dict = json.loads(content)
print(content)