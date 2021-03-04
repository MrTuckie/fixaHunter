import scrapy

'''

    TODO: Fazer um parse de url menos porco e que conte indefinidamente

'''


class FalabellaSpider(scrapy.Spider):
    name = 'falabella'
    allowed_domains = ['www.falabella.com']
    start_urls = ['https://www.falabella.com/falabella-cl/category/cat70007/Bicicletas?page=1']
    #start_urls = input("insira a sua url desejada: ")

    def parse(self, response):
        boxes = response.xpath("//div[@id='testId-searchResults-products']/div")
        for box in boxes:
            try:
                name = box.css("span>b::text").get()
                price = box.css("div[class*='cmr-icon-container']>span::text").get().strip("$  ")
                url = box.css("a::attr(href)").get()
                print(name,price,url)
                yield {
                    'name': name,
                    'price': price,
                    'url':  url,
                }
            except:
                pass
        
        # parsing next url
        nextUrl = response.url # '=' = 72 position
        urlList = nextUrl.split("=")
        number = int(urlList[1]) + 1
        nextUrl = urlList[0]+"="+str(number)
        nextUrl = ''.join(nextUrl)

        print("nexturl",nextUrl)

        yield scrapy.Request(url = nextUrl,callback=self.parse)      
