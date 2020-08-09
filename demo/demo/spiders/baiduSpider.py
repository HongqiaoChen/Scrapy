import scrapy


class BaiduspiderSpider(scrapy.Spider):
    name = 'baiduSpider'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):

        print(response.text)

        # print(response.headers)
        # print(response.status)

123123