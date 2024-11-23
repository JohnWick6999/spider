import urllib.request
import jsonpath
import json
import re

url = "https://www.taopiaopiao.com/cityAction.json?activityId&_ksTS=1731770194464_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true"
headers = {
    # ":authority": "www.taopiaopiao.com",
    # ":method": "GET",
    # ":path": "/cityAction.json?activityId&_ksTS=1731770194641_1088&jsonpCallback=jsonp1098&action=cityAction&s=new2&event_submit_doGetAllRegion=true",
    # ":scheme": "https",
    "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    # "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "bx-v": "2.5.22",
    "cookie": "cna=HfWH/Hb65TEASQjg5bUDU59_xIy_s-1; isg=BFTNTHCNMEmmvWQeLlRtFdBOHKgLqOgvgK63KphHlmjqG3vavTqlJD_C",
    "dnt": "1",
    "priority": "u=1,i",
    "referer": "https://www.taopiaopiao.com/?ptpm=3",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"NotA.Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.5 Safari/537.36 Edg/130.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
content = content.split("(")[1].split(")")[0]
# print(content)
with open("淘票票城市.json", "w", encoding="utf-8") as f:
    f.write(content)
get_city = json.load(open("淘票票城市.json", "r", encoding="utf-8"))
city_list = jsonpath.jsonpath(get_city, "$..regionName")
print(city_list)