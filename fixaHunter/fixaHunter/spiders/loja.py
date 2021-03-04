import scrapy


class LojaSpider(scrapy.Spider):
    name = 'loja'
    allowed_domains = ['mercadolivre.com.br']
    start_urls = ['http://mercadolivre.com.br/']

    def parse(self, response):
        pass
