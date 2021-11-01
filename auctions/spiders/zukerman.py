import scrapy
from scrapy import Request

from ..utils.parser import Parser
from ..items import AuctionsItem


class ZukermanSpider(scrapy.Spider):
    name = 'zukerman'
    parser = Parser()
    states_id, states_city_for_each_state = parser.get_states_id()

    start_urls = ['http://www.zukerman.com.br/']

    def parse(self, response):
        global data_bem_estado_id, data_bem_cidade_id, data_bem_categoria_id

        if self.city in self.states_id:
            estado = self.states_id[self.city]
            cidade = ''
        else:
            for state_id, state_cities in self.states_city_for_each_state.items():
                for city, city_id in state_cities.items():
                    if city == self.city:
                        estado = state_id
                        cidade = city_id

        url = f'https://www.zukerman.com.br/leilao-de-imoveis/{estado}/{cidade}'

        yield Request(url=url, callback=self.parse_response)

    def parse_response(self,response):
        item = AuctionsItem()

        divs = response.xpath('//div[@class="cd-0"]').extract()
        for div in divs:
            item['site'] = 'Zukerman'

            item['price'] = self.parser.get_single_value_from_string(raw_string=div, xpath='//li[@class="cd-it-r4-v1"]/text()').strip()

            url = self.parser.get_single_value_from_string(raw_string=div,xpath='//a/@href')
            item['url'] = url

            yield response.follow(url=url, callback=self.parse_description, cb_kwargs=item)

    def parse_description(self, response, **kwargs):
        item = kwargs

        description = response.xpath('//div[@class="s-d-ld-i1 f-d"]//p/text()').extract()
        description = ' '.join(description).strip()


        item['description'] = description

        item['category'] = self.parser.parse_category_based_on_description(description)

        yield item

