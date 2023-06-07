import scrapy


class AmazonspiderSpider(scrapy.Spider):
    name = "amazon_search_product"
   
    def start_requests(self): 
        keyword_list = ['socks']
        for keyword in keyword_list: 
            amazon_search_url = f'https://www.amazon.com/s?k={keyword}&page=1'
            yield scrapy.Request(url=amazon_search_url, callback = self.discover_product_urls, meta = {'keyword': keyword, 'page':1})

    def discover_product_urls(self,response):
        page = response.meta['page']
        keyword = response.meta['keyword']