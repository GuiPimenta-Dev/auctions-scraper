import scrapy

from ..items import AuctionsItem
from ..utils.parser import Parser


class LancenoleilaoSpider(scrapy.Spider):
    name = 'lancenoleilao'
    parser = Parser()

    states_id = {
        'sao_paulo': 'SP',
        'espirito_santo': 'ES',
        'mato_grosso_do_sul': 'MS',
        'parana': 'PA'
    }

    def __init__(self, city):

        if city in self.states_id:
            self.start_urls = [
                f'https://www.lancenoleilao.com.br/pesquisa.php?classificacao=1_0&uf={self.states_id[city]}',
                f'https://www.lancenoleilao.com.br/pesquisa.php?classificacao=1_1&uf={self.states_id[city]}',
                f'https://www.lancenoleilao.com.br/pesquisa.php?classificacao=1_2&uf={self.states_id[city]}',
                f'https://www.lancenoleilao.com.br/pesquisa.php?classificacao=1_3&uf={self.states_id[city]}'
            ]
        else:
            self.start_urls = [
                f'https://www.lancenoleilao.com.br/pesquisa.php?classificacao=1_0&uf=&cidade={city}',
                f'https://www.lancenoleilao.com.br/pesquisa.php?classificacao=1_1&uf=&cidade={city}',
                f'https://www.lancenoleilao.com.br/pesquisa.php?classificacao=1_2&uf=&cidade={city}',
                f'https://www.lancenoleilao.com.br/pesquisa.php?classificacao=1_3&uf=&cidade={city}'
            ]

    def parse(self, response):
        item = AuctionsItem()
        divs = response.xpath('//div[@class="mb-4 lotePadrao rounded lote-borda "]').extract()
        for div in divs:
            item['site'] = 'Lance no Leilão'

            item['price'] = 'R$ ' + self.parser.get_single_value_from_string(raw_string=div,
                                                                             xpath='//div[@class="col-lg-3 col-sm-12 lotePadraoValor"]/span/text()')

            id = self.parser.get_single_value_from_string(raw_string=div,
                                                          xpath='//div[@class="text-left text-center text-white py-1 back-7"]/@id')
            id = ''.join(char for char in id if char.isdigit())
            item['url'] = f'https://www.lancenoleilao.com.br/lote.php?idLote={id}'

            description = self.parser.get_single_value_from_string(raw_string=div,
                                                                   xpath='//p[@class="text-justify"]/text()')

            item['description'] = description

            item['category'] = self.parser.parse_category_based_on_description(description)

            yield item
