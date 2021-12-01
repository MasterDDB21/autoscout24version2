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

        #crawl to next page
        page=idea.css('h3.card-title a::attr(href)').extract_first()
        yield response.follow('https://ideas.lego.com'+page, self.parse)

        #example of xpath selector
        response.xpath('//*/a[text()[contains(.,"Go to next page")]]/../../div[3]/p/text()').extract()[0]

        #examples of copied selectors for nexpt page 
        #__next > div > div.css-xanrtl > div.css-160klfq.ey3mfx31 > main > div.css-1yuhvjn > nav > ul > li.css-jmbzf4 > a
        //*[@id="__next"]/div/div[4]/div[2]/main/div[15]/nav/ul/li[14]/a
        /html/body/div[1]/div[3]/div/div/div[4]/div[2]/main/div[15]/nav/ul/li[14]/a
        