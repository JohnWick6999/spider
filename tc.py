import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["sh.58.com"]
    start_urls = ["https://sh.58.com/sou/jh_%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91/"]

    def parse(self, response):
        content = response.text  # 获取响应的字符串
        content_b = response.body  # 获取二进制数据
        span = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]  # 直接使用xpath方法来使用response中的内容。
        print(span.extract())  # 提取selector对象的data属性值
        print(span.extract_first())  # 提取selector列表的第一个数据