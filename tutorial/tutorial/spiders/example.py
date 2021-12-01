import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['autoscout24.com']
    #   start_urls = [r"C:\Users\roblo\autoscout24\tutorial\Used cars for sale - AutoScout24.html"]
    start_urls = ['https://www.autoscout24.com/lst?sort=standard&desc=0&ustate=N%2CU&atype=C']
    #start_urls = ['https://www.autoscout24.com/lst/?sort=standard&desc=0&ustate=N%2CU&size=20&page=1&atype=C&']
    #start_urls = ["file:///C:/Users/roblo/autoscout24/tutorial/aap.htm"]

    def parse(self, response):
        for article in response.css('main article.cldt-summary-full-item'):
            yield {
                'url': response.url,        #include url in database for future reference
                'title': article.css('h2').xpath('normalize-space()').extract(),
                'subtitle': article.css('span span').xpath('normalize-space()').extract(),

            }
