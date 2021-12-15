import scrapy
from selenium import webdriver
import time
from scrapy.selector import Selector

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['autoscout24.com']
    #   start_urls = [r"C:\Users\roblo\autoscout24\tutorial\Used cars for sale - AutoScout24.html"]
    #    start_urls = [#'https://www.autoscout24.com/lst?sort=standard&desc=0&ustate=N%2CU&atype=C'#]
    #                    'https://www.autoscout24.com/lst/?sort=standard&desc=0&ustate=N%2CU&size=20&page=1&atype=C&',
                    #'https://www.autoscout24.com/lst/?sort=standard&desc=0&ustate=N%2CU&size=20&page=2&atype=C&',
    #                    'https://www.autoscout24.com/lst/?sort=standard&desc=0&ustate=N%2CU&size=20&page=3&atype=C&',
    #                    'https://www.autoscout24.com/lst/?sort=standard&desc=0&ustate=N%2CU&size=20&page=4&atype=C&',
    #                    'https://www.autoscout24.com/lst/?sort=standard&desc=0&ustate=N%2CU&size=20&page=5&atype=C&',
                  # 'file:///C:/Users/roblo/autoscout24/tutorial/locallyStoredWebPage.html'
    #                ]
    start_urls = ['https://www.autoscout24.com/lst/?sort=standard&desc=0&ustate=N%2CU&size=20&page=1&atype=C&']
    #start_urls = ["file:///C:/Users/roblo/autoscout24/tutorial/aap.htm"]

    #Initalize the webdriver that needs to run when you use selenium   
    def __init__(self):
        #add chromedriver_binary to path in order to run
        #(nationalevacaturebank) C:\Users\roblo\nationalevacaturebank\tutorial>set PATH=%PATH%;C:\Users\roblo\AppData\Local\conda\conda\envs\nationalevacaturebank\Lib\site-packages\chromedriver_binary

        #start up
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5) # wait maximally 10 seconds; see https://selenium-python.readthedocs.io/waits.html
        time.sleep(5)
                
    def get_selenium_response(self, url):
        self.driver.get(url)
        time.sleep(5)

        # #Program robustly here because errors may occur at 1st line (for example, the logical error, when the webpage does not have a button); 
        # #If an error eventually occurs then the try/except structure will cause the code to run anyways without any hinderance of stopping the scraping process.
        # try:
        #     #click button
        #     # python_button = self.driver.find_elements_by_xpath('SPECIFY; EXAMPLE: //*[@id="form_save"]')[0]
        #     # python_button.click()

        #     #example of xpath selector
        #     response.xpath('//*/a[text()[contains(.,"Go to next page")]]/../../div[3]/p/text()').extract()

        #     time.sleep(10)  #time lets the browser wait during the specified number of seconds
        # except:
        #     pass

        #return encoded page that is accessable after the click
        return self.driver.page_source.encode('utf-8')

    def parse(self, response):
        # Here you got response from webdriver
        # you can use selectors to extract data from it
        url=response.url
        selenium_response = Selector(text=self.get_selenium_response(url))
        #time.sleep(15)

        #open csv files that you already scraped
        #read in the data within 1st column---assuming that that holds url
        #store in a list

        # if True:
        #     for article in response.css('main article.cldt-summary-full-item'):
        #         yield {
        #             'url': response.url,        #include url in database for future reference
        #             'title': article.css('h2').xpath('normalize-space()').extract(),
        #             'subtitle': article.css('span span').xpath('normalize-space()').extract(),

        #             #compare new url to old ones from csv files
        #             #if u already have then do not scrape the new data---technically check if break will do what u want
        #         }

        #crawl to next page
        ###CAREFUL: results in an url that may cause a 400 because of bad syntax:
        #https://www.autoscout24.com/    +     ?&sort=standard&desc=0&ustate=N%2CU&size=20&atype=C&page=3
        #REMEDY: https://www.autoscout24.com/lst/    +   ... IS OKAY!
        #page=idea.css('h3.card-title a::attr(href)').extract_first()
        page=selenium_response.xpath('//*/a[text()[contains(.,"Next")]]/@href').extract_first()
        #yield response.follow('https://ideas.lego.com'+page, self.parse)
        # page=response.xpath('//*/a[text()[contains(.,"Next")]]/@href').extract_first()
        print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"+page)
        yield response.follow('https://www.autoscout24.com/lst/'+page, self.parse)

        #self.driver.close()

        #example of xpath selector
        #response.xpath('//*/a[text()[contains(.,"Go to next page")]]/../../div[3]/p/text()').extract()
        #print("SINTERKLAASJE:")
        # yield {
        #     #'nextPage': selenium_response.xpath('//*/a[text()[contains(.,"Go to next page")]]/../../div[3]/p/text()').extract(),
        #     #'nextPageSimplified': selenium_response.xpath('//*/a[text()[contains(.,"Go to next page")]]').extract(),
        #     'nextPageSimplified2': selenium_response.xpath('//*/a[text()[contains(.,"Next")]]/@href').extract(),
        #     #'nextPage1': selenium_response.css('#__next > div > div.css-xanrtl > div.css-160klfq.ey3mfx31 > main > div.css-1yuhvjn > nav > ul > li.css-jmbzf4 > a').extract(),
        #     #'nextPage2': selenium_response.xpath('//*[@id="__next"]/div/div[4]/div[2]/main/div[15]/nav/ul/li[5]/a').extract(),
        # }

        #examples of copied selectors for nexpt page 
        #__next > div > div.css-xanrtl > div.css-160klfq.ey3mfx31 > main > div.css-1yuhvjn > nav > ul > li.css-jmbzf4 > a
        #//*[@id="__next"]/div/div[4]/div[2]/main/div[15]/nav/ul/li[14]/a
        #/html/body/div[1]/div[3]/div/div/div[4]/div[2]/main/div[15]/nav/ul/li[14]/a
