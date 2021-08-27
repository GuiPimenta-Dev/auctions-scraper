import scrapy
from scrapy import FormRequest
from ..items import AuctionsItem
from ..utils.parser import Parser


class SodresantoroSpider(scrapy.Spider):
    name = 'sodresantoro'
    parser = Parser()

    def __init__(self, city):
        if city == 'sao_paulo':
            self.start_urls = ['https://www.sodresantoro.com.br/']

    def parse(self, response):
        data = {
            'ajax_filtro': '2',
            'filtros[tipo]': '',
            'filtros[segmento]': '3',
            'filtros[deposito]': 'São Paulo;São Paulo - SP;SÃO PAULO -SP;São Paulo- SP;SP',
            'filtros[data]': ''
        }

        url = 'https://www.sodresantoro.com.br/'

        yield FormRequest(url=url, formdata=data, callback=self.parse_response)

    def parse_response(self, response):  # sourcery skip: aug-assign
        item = AuctionsItem()
        hrefs = response.xpath('//li[@class="leilao_visualizacao-4"]//a[@class="descricao"]/@href').extract()
        for href in hrefs:
            item['site'] = 'Sodré Santoro'

            url = 'https://www.sodresantoro.com.br'
            url += href
            item['url'] = url

            yield response.follow(url=url, callback=self.parse_price_and_description, cb_kwargs=item)

    def parse_price_and_description(self, response, **kwargs):
        item = kwargs

        item['price'] = response.xpath('//b[@class="lance"]/text()').get()

        description = response.xpath('//h2[@class="titulo_1"]/text()').get()
        item['description'] = description

        item['category'] = self.parser.parse_category_based_on_description(description)

        yield item
