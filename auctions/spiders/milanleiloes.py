import scrapy
from scrapy import FormRequest

from ..items import AuctionsItem
from ..utils.parser import Parser


class MilanleiloesSpider(scrapy.Spider):
    name = 'milanleiloes'
    parser = Parser()

    amazonas_opt = """<select name="selCidades" id="selCidades" style="width:250px;"><option value="">Todas</option>
                    
                <option>Manaus </option></select>"""
    bahia_opt = """<select name="selCidades" id="selCidades" style="width:250px;"><option value="">Todas</option>
                    
                <option>Eunápolis</option><option>Porto Seguro</option><option>Salvador </option></select>"""
    es_opt = """<select name="selCidades" id="selCidades" style="width:250px;"><option value="">Todas</option>
                    
                <option>Vila Velha </option></select>"""
    maranhao_opt = """<select name="selCidades" id="selCidades" style="width:250px;"><option value="">Todas</option>
                    
                <option>Estreito</option><option>Imperatriz</option><option>São   Luís</option></select>"""
    minas_gerais_opt = """<select name="selCidades" id="selCidades" style="width:250px;"><option value="">Todas</option>
                    
                <option>Bicas </option><option>Muriaé </option></select>"""
    mgs_opt = """<select name="selCidades" id="selCidades" style="width:250px;"><option value="">Todas</option>
                    
                <option>Campo Grande</option></select>"""
    pernambuco_opt = """<select name="selCidades" id="selCidades" style="width:250px;"><option value="">Todas</option>
                    
                <option>Jaboatão dos Guararapes</option></select>"""
    parana_opt = """<select name="selCidades" id="selCidades" style="width:250px;"><option value="">Todas</option>
                    
                <option>Campo Mourão </option><option>Curitiba </option></select>"""
    rj_opt = """<select name="selCidades" id="selCidades" style="width:250px;"><option value="">Todas</option>
                    
                <option>Cachoeiras de Macacu </option><option>Itaboraí </option><option>Rio de Janeiro </option><option>São Gonçalo </option></select>"""
    sp_opt = """<select name="selCidades" id="selCidades" style="width:250px;"><option value="">Todas</option>
                    
                <option>Agudos </option><option>Alvares Florence </option><option>Araraquara </option><option>Bebedouro </option><option>Guarujá </option><option>Itapevi</option><option>Itaquaquecetuba </option><option>Marília </option><option>Salto</option><option>Santos</option><option>São Bernardo do Campo</option><option>São Carlos </option><option>São Paulo </option><option>Taubaté</option></select>"""

    states_id = {
        'amazonas': 'AM',
        'bahia': 'BA',
        'espirito_santo': 'ES',
        'maranhao': 'MA',
        'minas_gerais': 'MG',
        'mato_grosso_do_sul': 'MS',
        'pernambuco': 'PE',
        'parana': 'PR',
        'rio_de_janeiro': 'RJ',
        'sao_paulo': 'SP'
    }
    amazonas_cities_id = parser.parse_select_dict_without_values(amazonas_opt)
    bahia_cities_id = parser.parse_select_dict_without_values(bahia_opt)
    es_cities_id = parser.parse_select_dict_without_values(es_opt)
    maranhao_cities_id = parser.parse_select_dict_without_values(maranhao_opt)
    minas_gerais_cities_id = parser.parse_select_dict_without_values(minas_gerais_opt)
    mgs_cities_id = parser.parse_select_dict_without_values(mgs_opt)
    pernambuco_cities_id = parser.parse_select_dict_without_values(pernambuco_opt)
    parana_cities_id = parser.parse_select_dict_without_values(parana_opt)
    rj_cities_id = parser.parse_select_dict_without_values(rj_opt)
    sp_cities_id = parser.parse_select_dict_without_values(sp_opt)

    states_city_for_each_state = {
        states_id['amazonas']: amazonas_cities_id,
        states_id['bahia']: bahia_cities_id,
        states_id['espirito_santo']: es_cities_id,
        states_id['maranhao']: maranhao_cities_id,
        states_id['mato_grosso_do_sul']: mgs_cities_id,
        states_id['minas_gerais']: minas_gerais_cities_id,
        states_id['parana']: parana_cities_id,
        states_id['pernambuco']: pernambuco_cities_id,
        states_id['rio_de_janeiro']: rj_cities_id,
        states_id['sao_paulo']: sp_cities_id,
    }

    start_urls = ['https://www.milanleiloes.com.br/']

    def parse(self, response):
        global sel_uf, sel_cidades

        if self.city in self.states_id:
            sel_uf = self.states_id[self.city]
            sel_cidades = ''
        else:
            for state_id, state_cities in self.states_city_for_each_state.items():
                for city in state_cities:
                    if self.parser.normalize_string(city) == self.city:
                        sel_uf = state_id
                        sel_cidades = city

        data = {
            'selUF': sel_uf,
            'selCidades': sel_cidades,
            'txtBuscaDescricao': '',
            'btnProcurarImovel': 'Procurar'
        }

        url = 'https://www.milanleiloes.com.br/Busca/BuscaImoveis.asp'

        yield FormRequest(url=url, formdata=data, callback=self.parse_response)

    def parse_response(self, response):
        item = AuctionsItem()
        trs = response.xpath('//table[@class="general_table"]//tr').extract()
        for tr in trs:
            button = self.parser.get_single_value_from_string(raw_string=tr, xpath='//a/@href')
            if button:
                item['site'] = 'Milan Leilões'

                item['price'] = '-'

                if 'javascript' in button:
                    cl = button.partition('(')[-1].split(',')[0]
                    lote = self.parser.get_single_value_from_string(raw_string=tr, xpath='//td/text()')
                    url = f'https://www.milanleiloes.com.br/Leiloes/Lance/lote.asp?CL={cl}#Lote={lote}'

                else:
                    url = 'https://www.milanleiloes.com.br' + button

                item['url'] = url

                description = self.parser.get_single_value_from_string(raw_string=tr, xpath='//td[2]')
                item['description'] = self.parser.clean_html_tags_from_string(description)

                yield item