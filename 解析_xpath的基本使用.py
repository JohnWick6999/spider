from lxml import etree

# 解析
# (1)本地文件                                           etree.parse()
# (2)服务器响应的数据 response.read().decode("UTF-8")    etree.HTML()

# xpath解析本地文件
# xpath遵守HTML规范，需要在单标签后添加对应的结束字符“/”
tree = etree.parse("解析_xpath的基本使用.html")
# print(tree)
# tree.xpath("xpath路径")

# 查找ul下面的li
# li_list = tree.xpath("//body/ul/li")

# 查找所有带有id属性的li标签
# text() 获取标签中的内容
# li_list = tree.xpath("//ul/li[@id]/text()")

# 找到id为l1的li标签，注意引号问题。
# li_list = tree.xpath("//ul/li[@id='l1']/text()")

# 查找id为l1的li标签的class属性值
# li = tree.xpath("//ul/li[@id='l1']/@class")

# 模糊查询  contains(),starts-with()
# 查询id中包含l的li标签，注意引号问题。
# li_list = tree.xpath("//ul/li[contains(@id,'l')]/text() ")
# 查询id的值以l开头的标签，注意引号问题。
# li_list = tree.xpath("//ul/li[starts-with(@id,'c')]/text()")

# 逻辑运算    与：and   或："标签 | 标签"
# 查询id为l1且class为c1的数据
# li_list = tree.xpath("//ul/li[@id='l1' and @class='c1']/text()")
li_list = tree.xpath("//ul/li[@id='l1']/text() | //ul/li[@id='l2']/text()")
print(li_list)
# 判断列表的长度
print(len(li_list))