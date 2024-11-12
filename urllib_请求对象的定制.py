#UA反爬
import urllib.request

url = "https://www.baidu.com"

#url的组成
#http/https     www.baidu.com      http:80,https:443,mysql:3306,oracle:1521,redis:6379,mongodb:27017
#协议                 主机                          端口号
#除了上面三个以外，还有：路径(s)，参数(wd = ...)，锚点

#UA 用户代理
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/13"
}

#因为urlopen中存放不了字典，所以headers传不进去。
#请求对象的定制
#注意传参顺序问题！！！
request = urllib.request.Request(url = url,headers = headers)

response = urllib.request.urlopen(request)
content = response.read().decode("UTF-8")
print(content)