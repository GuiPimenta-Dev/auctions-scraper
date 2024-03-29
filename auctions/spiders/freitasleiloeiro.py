import scrapy
from ..items import AuctionsItem
from ..utils.parser import Parser
from ..constants.constants import GroundTypeEnum as GTEnum


class FreitasleiloeiroSpider(scrapy.Spider):
    name = 'freitasleiloeiro'
    parser = Parser()
    states_id, states_city_for_each_state = parser.get_states_id()

    # states_id = {
    #     'goias': 'GO',
    #     'parana': 'PR',
    #     'rio_grande_do_sul': 'RS',
    #     'sao_paulo': 'SP'
    # }
    #
    # goias_cities_id = {
    #     'goiania': 'GOIANIA',
    #     'goias': 'GOIAS',
    # }
    #
    # parana_cities_id = {
    #     'guaira': 'GUAIRA',
    # }
    #
    # rgs_cities_id = {
    #     'porto_alegre': 'PORTO ALEGRE'
    # }
    #
    # sp_cities_id = {
    #     'brauna': 'BRAUNA',
    #     'candido_mota': 'CANDIDO MOTA',
    #     'sao_bernardo_do_campo': 'SAO BERNARDO DO CAMPO'
    # }
    #
    # states_city_for_each_state = {
    #     states_id['goias']: goias_cities_id,
    #     states_id['parana']: parana_cities_id,
    #     states_id['rio_grande_do_sul']: rgs_cities_id,
    #     states_id['sao_paulo']: sp_cities_id,
    # }

    def __init__(self, city):

        sub_category_param = ''

        if city in self.states_id:
            state_param = self.states_id[city].upper()
            city_param = ''
        else:
            for state_id, state_cities in self.states_city_for_each_state.items():
                for city_key, city_id in state_cities.items():
                    if city_key == city:
                        state_param = state_id.upper()
                        city_param = city_id.upper().replace('-', ' ')

        category_param = '2'

        self.start_urls = [
            f'https://www.freitasleiloeiro.com.br/leiloes/pesquisar?query=&categoria={category_param}&subCategoria={sub_category_param}&subCategoriaLabel=Im%C3%B3veis%20Comerciais&estado={state_param}&cidade={city_param}']

    def parse(self, response):
        item = AuctionsItem()
        trs = response.xpath('//tr[@class="cursor-pointer bradesco"]').extract()
        for tr in trs:
            item['site'] = 'Freitas Leiloeiro'

            item['price'] = self.parser.get_single_value_from_string(raw_string=tr,
                                                                     xpath='//td[3]//strong/text()').strip()

            item['url'] = 'https://www.freitasleiloeiro.com.br' + self.parser.get_single_value_from_string(
                raw_string=tr, xpath='//a/@href')

            description = self.parser.get_multiple_values_from_string(raw_string=tr,
                                                                      xpath='//div[@class="text-justify;"]/text()')
            description = self.parser.clean_html_tags_from_string(description)
            item['description'] = description

            item['category'] = self.parser.parse_category_based_on_description(description)

            yield item
