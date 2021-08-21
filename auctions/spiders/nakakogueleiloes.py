import scrapy
from scrapy import FormRequest



class NakakogueleiloesSpider(scrapy.Spider):
    name = 'nakakogueleiloes'
    start_urls = ['https://www.nakakogueleiloes.com.br/lotes/consulta/1/']

    def parse(self, response):
        data = {
            "cmp-buscar": "Jacarezinho"
        }
        url = 'https://www.nakakogueleiloes.com.br/lotes/consulta/1/'

        yield FormRequest(url=url, formdata=data, callback=self.parse_response)

    def parse_response(self, response):
        pass



