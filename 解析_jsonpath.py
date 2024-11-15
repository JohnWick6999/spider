import json
import jsonpath
# jsonpath只能解析本地json数据
# 本案例解析文件详见"jsonpath.json"
obj = json.load(open("jsonpath.json", "r", encoding="utf-8"))
print(obj)

# 所有书的作者
author_list = jsonpath.jsonpath(obj, "$.store.book[*].author")
print(author_list)

# 所有的作者
author_list = jsonpath.jsonpath(obj, "$..author")
print(author_list)

# store下面的所有元素
store_list = jsonpath.jsonpath(obj, "$.store.*")
print(store_list)

# store里所有的price
store_price_list = jsonpath.jsonpath(obj, "$.store..price")
print(store_price_list)

# 第三本书
get_third_book = jsonpath.jsonpath(obj, "$..book[2]")
print(get_third_book)

# 最后一本书
get_last_book = jsonpath.jsonpath(obj, "$..book[(@.length-1)]")
print(get_last_book)

# 前两本书，写成[0,1]这种形式也可以
get_fs_books = jsonpath.jsonpath(obj, "$..book[:2]")
print(get_fs_books)

# 条件过滤需要在"()"前面添加"?"
# 过滤出所有包含isbn的书
find_isbn_book = jsonpath.jsonpath(obj, "$..book[?(@.isbn)]")
print(find_isbn_book)

# 哪本书超过了10元?
find_price_up10_book = jsonpath.jsonpath(obj, "$..book[?(@.price>10)]")
print(find_price_up10_book)