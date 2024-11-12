# 获取豆瓣电影动作片排行榜第一页的数据，并且保存起来。
# get请求
import urllib.request

url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/13"
}

request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("UTF-8")
# print(content)

f = open("douban.json","w",encoding="UTF-8")
f.write(content)
f.close()