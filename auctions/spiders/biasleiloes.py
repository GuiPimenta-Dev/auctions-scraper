import scrapy
from scrapy import Request

from ..items import AuctionsItem
from ..utils.parser import Parser


class BiasleiloesSpider(scrapy.Spider):
    name = 'biasleiloes'
    parser = Parser()
    states_id, states_city_for_each_state = parser.get_states_id()

    start_urls = ['https://www.biasileiloes.com.br/']

    def parse(self, response):
        global data_bem_estado_id, data_bem_cidade_id, data_bem_categoria_id

        if self.city in self.states_id:
            data_bem_estado_id = self.states_id[self.city]
            data_bem_cidade_id = 'todas-as-cidades'
        else:
            for state_id, state_cities in self.states_city_for_each_state.items():
                for city, city_id in state_cities.items():
                    before, _, _ = city.partition('_(')
                    if before == self.city:
                        data_bem_estado_id = state_id
                        data_bem_cidade_id = before.replace('_', '-')
                        pass


        subclasse = 'todos-os-segmentos'

        token = response.xpath('//input[@name="__RequestVerificationToken"]/@value').get()

        url = f'https://www.biasileiloes.com.br/Sale/LotListSearch?categoria=&subcategoria=&term=&start=0&limit=20&listaId=&slug=&buscaImovel=true&estado={data_bem_estado_id}&bairro=todos-os-bairros&cidade={data_bem_cidade_id}&segmento={subclasse}&__RequestVerificationToken={token}'

        yield Request(url=url, callback=self.parse_response)

    def parse_response(self, response):
        item = AuctionsItem()
        divs = response.xpath('//div[@class="thumbnail thumbnail-vitrine-lot item-bid "]').extract()
        for div in divs:
            item['site'] = 'Bias Leilões'

            item['price'] = self.parser.get_single_value_from_string(raw_string=div,
                                                                     xpath='//span[@class="price-line"]/text()')

            item['url'] = 'https://www.biasileiloes.com.br/' + self.parser.get_single_value_from_string(raw_string=div,
                                                                                                        xpath='//a/@href')

            description = self.parser.get_single_value_from_string(raw_string=div,
                                                                           xpath='//div[@class="photo-text"]/span/text()')

            item['description'] = description

            item['category'] = self.parser.parse_category_based_on_description(description)

            yield item
