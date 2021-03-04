import scrapy


class OlxSpider(scrapy.Spider):
    name = 'olx'
    allowed_domains = ['olx.com.br']
    start_urls = ['https://www.olx.com.br/anuncios/misc/bikes-fixas?f=keyword:bikes-fixas&pageNumber=1']

    def parse(self, response):
        boxes = response.xpath("//div[@class='result-product-row']")   
        for box in boxes:
            try:
                url = box.xpath("../@href").get()
                name = box.css("div.result-product-info > h2::text").get().strip()
                description = box.css("div.result-product-info > p::text").get().strip()
                price = box.css("div.result-product-price::text").get().strip("R$ ").strip()
                #print(name,description,price)
                yield{
                    'name' : name,
                    'description' : description,
                    'price':price,
                    'url': url,
                }
            except:
                pass


        # parsing next url
        nextUrl = list(response.url)
        index = int(nextUrl[-1]) + 1
        nextUrl[-1] = str(index)
        nextUrl = ''.join(nextUrl)
        print("nexturl",nextUrl)

        yield scrapy.Request(url = nextUrl,callback=self.parse)