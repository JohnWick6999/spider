import urllib.request
from lxml import etree
import time

# https://sc.chinaz.com/tupian/fengjing.html (1)
# https://sc.chinaz.com/tupian/fengjing_2.html (2)
# https://sc.chinaz.com/tupian/fengjing_3.html (3)
# https://sc.chinaz.com/tupian/fengjing_page.html 除了第一页的网址

def creat_request(page):
    if page == 1:
        url = "https://sc.chinaz.com/tupian/fengjing.html"
    else:
        url = f"https://sc.chinaz.com/tupian/fengjing_{page}.html"
    # print(url)
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
    }
    request = urllib.request.Request(url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("UTF-8")
    return content

def download(content):
    tree = etree.HTML(content)
    # 特别的，对于页面有懒加载的情况，要选定懒加载原始的代码。
    find_pic_url = tree.xpath('//div/img/@data-original')
    find_pic_name = tree.xpath('//div/img/@alt')
    # print(len(find_pic_url),len(find_pic_name))
    for i in range(len(find_pic_url)):
        # print(find_pic_url[i], find_pic_name[i])
        urllib.request.urlretrieve(f"https:{find_pic_url[i].replace("_s","")}",f"./GetPicture/{find_pic_name[i]}.jpeg")
        time.sleep(0.1)
if __name__ == '__main__':
    start_page = int(input("起始页："))
    end_page = int(input("结束页："))
    for x in range(start_page, end_page+1):
        # print(x)
        request = creat_request(x)
        content = get_content(request)
        download(content)