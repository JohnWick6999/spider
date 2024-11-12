from urllib import request

#下载网页   参数url代表的是下载的路径，filename是文件的名字
# url_page = "http://www.baidu.com"
# request.urlretrieve(url_page, "baidu.html")

#下载图片
# url_image = "https://www.rollingstone.com/wp-content/uploads/2020/02/TheWeeknd.jpg"
# request.urlretrieve(url = url_image,filename = "The Weeknd.jpeg")

#下载视频
url_video = "https://vd3.bdstatic.com/mda-qij1fmkvjnq65r34/576p/h264/1726794115112581004/mda-qij1fmkvjnq65r34.mp4"
request.urlretrieve(url_video, "Die for you.mp4")