import scrapy
from bs4 import BeautifulSoup
from scrapy import FormRequest

from ..items import AuctionsItem
from ..utils.parser import Parser


class KronbergleiloesSpider(scrapy.Spider):
    name = 'kronbergleiloes'
    parser = Parser()
    id_tipo = '10'
    id_subtipo = {"rural": '52', "industrial": '50', "residencial": '51', "comercial": '49', "terreno": '90'}
    id_cidades = {'agudos_do_sul': '123', 'apiacas': '445', 'apucarana': '457', 'arapongas': '528', 'ararangua': '541',
                  'araucaria': '562', 'bandeirantes': '777', 'bituruna': '1036', 'bocaiuva_do_sul': '1096',
                  'cambe': '1521', 'campina_grande_do_sul': '1557', 'campo_largo': '1594', 'cascavel': '1890',
                  'cianorte': '2056', 'colombo': '2125', 'cornelio_procopio': '2262', 'cruz_machado': '2403',
                  'cruzeiro_do_oeste': '2415', 'curimata': '2455', 'curitiba': '2458', 'curiuva': '2460',
                  'eneas_marques': '2697', 'fazenda_rio_grande': '2876', 'figueira': '2925', 'foz_do_iguacu': '3002',
                  'francisco_beltrao': '3011', 'general_carneiro': '3108', 'guarapuava': '3298', 'guaratuba': '3308',
                  'ilhabela': '3563', 'irati': '3717', 'jaguariaiva': '4078', 'joaquim_tavora': '4228',
                  'londrina': '4523', 'mandirituba': '4664', 'marechal_candido_rondon': '4752', 'maringa': '4788',
                  'matinhos': '4866', 'maua_da_serra': '4886', 'nova_lima': '5398', 'ortigueira': '5565',
                  'palmas': '5675', 'paula_freitas': '5884', 'perobal': '6019', 'pinhais': '6097',
                  'pirai_do_sul': '6154', 'ponta_grossa': '6286', 'pontal_do_parana': '6290', 'porto_uniao': '6404',
                  'quitandinha': '6582', 'reserva': '6652', 'rio_negro': '6808', 'rolandia': '6867',
                  'sao_jose_dos_pinhais': '7709', 'sao_paulo': '7791', 'sao_tome': '7888', 'sapopema': '7921',
                  'tapejara': '8320', 'terra_boa': '8424', 'terra_roxa': '8433', 'tijucas_do_sul': '8453',
                  'tres_barras': '8531', 'umuarama': '8677', 'uniao_da_vitoria': '8681', 'wenceslau_braz': '8997'}

    start_urls = ['https://www.kronbergleiloes.com.br/']

    def parse(self, response):
        data = {
            "id_tipo_lote": self.id_tipo,
            "id_subtipo": self.id_subtipo['residencial'],
            "estado": '',
            "id_cidades": self.id_cidades['colombo'],
            'Ped': 'Pesquisar'
        }

        url = 'https://www.kronbergleiloes.com.br/leilao/busca'

        yield FormRequest(url=url, formdata=data,
                          callback=self.parse_auction_response)

    def parse_auction_response(self, response):
        item = AuctionsItem()

        divs = response.xpath('//div[@class="bid-details"]').extract()
        for index, div in enumerate(divs):
            item['site'] = 'Kronberg Leilões'
            item['price'] = BeautifulSoup(response.xpath('//div[@class="linha-valor-leilao active"]').extract()[index],
                                           features="lxml").get_text(strip=True).split(':')[1]
            item['url'] = self.parser.parse_string_to_html(raw_string=div, xpath='//a/@href')

            item['description'] = self.parser.parse_string_to_html(raw_string=div, xpath='//a/text()')

            yield item

