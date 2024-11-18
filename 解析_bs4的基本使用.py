from bs4 import BeautifulSoup

# 解析本地文件
# 默认打开编码格式为gbk
soup = BeautifulSoup(open("解析_bs4的基本使用.html", encoding="utf-8"), "lxml")
# print(soup)


# 根据标签名查找结点
# 找到的是第一个符合条件的数据
print(soup.a)
# attrs获取标签的属性和属性值
print(soup.a.attrs)

# bs4的一些函数

# 1.find
#   返回的是第一个符合条件的数据
print(soup.find("a"))
#   根据title的值找到对相应的标签对象
print(soup.find("a", title="a2"))
# 根据class的值找到对相应的标签对象 注意"class"需要添加下划线以避免与class关键字冲突
print(soup.find("a", class_="a1"))

# 2.find_all
#   返回的是一个列表，并且返回了所有指定的标签。
print(soup.find_all("a"))
#   特别的，对于指定了多种标签的情况下，应将它们放入同一个列表中。
print(soup.find_all(["a", "span"]))
#   limit参数  limit=?,那就找到第?个标签
print(soup.find_all("li", limit=3))

# 3.select  推荐使用
#   select方法返回的是一个列表，并且会将多个与条件匹配的数据封装到列表中。
print(soup.select("a"))

# 类选择器
#   soup.select(".class_value")
print(soup.select(".a1"))
# soup.select("#id_value")
print(soup.select("#l1"))

# 属性选择器-----通过属性寻找对应的标签
# 查找li标签中有id的标签
print(soup.select("li[id]"))
# 查找li标签中id为l2的标签
print(soup.select("li[id='l2']"))

# 层级选择器     " "  ">"  ","
#   后代选择器 " "(空格)
#   找到的是div标签下面的li标签
print(soup.select("div li"))

# 子代选择器 ">"
#   寻找某标签的第一级子标签
#   注意：很多计算机编程语言中，如果不加空格不会输出内容，但是在bs4中不会报错，会正确地输出内容。
print(soup.select("div>ul>li"))

#   找到a标签和li标签所有的对象 ","   与soup.find_all(["k1","k2"])意义相近
print(soup.select("a,li"))

# 节点信息
#   获取节点内容
"""如果标签对象中只有内容，那么string和get_text()都可以使用
如果标签对象中出来内容还有标签，那么string就获取不到数据，而get_text()是可以获取到数据的。
所以一般情况下，推荐使用get_text()"""
obj = soup.select("#d1")[0]
print(obj.string)
print(obj.get_text())

# 节点的属性
obj = soup.select("#p1")[0]
#   name是标签的名字
print(obj.name)
#   将指定标签的属性值封装进字典并返回
print(obj.attrs)

# 获取节点的属性
obj = soup.select("#p1")[0]

print(obj.attrs.get("class"))
print(obj.get("class"))
print(obj["class"])