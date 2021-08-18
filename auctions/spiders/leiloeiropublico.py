import scrapy


class LeiloeiropublicoSpider(scrapy.Spider):
    name = 'leiloeiropublico'
    start_urls = ['https://leiloeiro-publico.negocio.site/']

    def parse(self, response):
        pass
