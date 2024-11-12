# 第1页
# https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10

# 第二页
# https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10

import urllib.parse
import urllib.request

base_url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"

def creat_request(page):
    base_url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    data = {
        "cname": "北京",
        "pid":"",
        "pageIndex": page,
        "pageSize": "10"
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
    }
    request = urllib.request.Request(base_url, data, headers)
    return request
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content

def download(page,content):
    with open("kfc_" + str(page) + ".json","w",encoding= "UTF-8") as f:
        f.write(content)
if __name__ == '__main__':
    start_page = int(input("起始页："))
    end_page = int(input("结束页："))
    for page in range(start_page, end_page + 1):
        request = creat_request(page)
        content = get_content(request)
        download(page,content)