import scrapy


class TopoleiloesSpider(scrapy.Spider):
    name = 'topoleiloes'
    city = {'antonina'}
    start_urls = ['https://topoleiloes.com.br/busca?cidade=3925&categoria=3']

    def parse(self, response):
        pass
