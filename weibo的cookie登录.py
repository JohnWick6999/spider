import urllib.request

url = "https://weibo.cn/6352818729/info"
# key开头带有冒号的或者是"accept-encoding"都要注释掉。
headers = {
    # ":authority": "weibo.cn",
    # ":method": "GET",
    # ":path": "/6352818729/info",
    # ":scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    # cookie中携带着登录信息
    "cookie": "_T_WM=7cd74b1536d2d145b051af5281ceee6e; SCF=AhWhxLLCTzwHp2oSTZHLLUcgmIfxPnFvDmPS7YnebPQ2xMiThOwkH45SG_gwBCq7zLPbLSdeUTQxDLIe7L70uJI.; SUB=_2A25KK2uNDeRhGeBN7lAZ8SbLyTWIHXVpSeFFrDV6PUJbktANLRDmkW1NREnYs5JglPQwriWDHJqp_NqAs00pPyaC; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWJ0KhkJYEcBkjlAKzNLXBG5NHD95Qce0-E1h2RS0z4Ws4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSoefeonp1hME1Btt; SSOLoginState=1731140573; ALF=1733732573",
    "dnt": "1",
    "priority": "u=0, i",
    # referer判断当前路径是不是从上一个路径进来的，如果url不是从referer所指定的的链接进入的，就报错了。
    # 一般情况下，referer用于做图片防盗链。
    "referer": "https://weibo.cn/",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
# 登陆页面的编码
content = response.read().decode('utf-8')
# print(content)
with open('weibo.html', 'w',encoding="utf-8") as f:
    f.write(content)