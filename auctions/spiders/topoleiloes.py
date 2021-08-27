import scrapy
from ..constants.constants import GroundTypeEnum as GTEnum
from ..items import AuctionsItem
from ..utils.parser import Parser


class TopoleiloesSpider(scrapy.Spider):
    name = 'topoleiloes'
    citys_id = {'antonina': '3925', 'curitiba': '4004', 'goioxim': '4036', 'guaratuba': '4047', 'honorio_serpa': '4048',
                'irati': '4063', 'jataizinho': '4086', 'pinhais': '4175', 'ponta_grossa': '4185',
                'sao_jose_dos_pinhais': '4260',
                'porto_alegre': '4927', 'blumenau': '4346'}
    parser = Parser()

    def __init__(self, city):
        if city in self.citys_id:
            self.start_urls = [
                f'https://topoleiloes.com.br/busca?cidade={self.citys_id[city]}&categoria=3',
                f'https://topoleiloes.com.br/busca?cidade={self.citys_id[city]}&categoria=4',
                f'https://topoleiloes.com.br/busca?cidade={self.citys_id[city]}&categoria=5',
                f'https://topoleiloes.com.br/busca?cidade={self.citys_id[city]}&categoria=6',
                f'https://topoleiloes.com.br/busca?cidade={self.citys_id[city]}&categoria=12',
            ]

    def parse(self, response):
        item = AuctionsItem()

        divs = response.xpath('//div[@class="listing-item evo-pix-box"]').extract()
        for div in divs:
            item['site'] = 'Topo Leilões'
            price = self.parser.get_multiple_values_from_string(raw_string=div,
                                                                xpath='//ul[@class="listing-details-valores"]//li')
            _, dollar_sign, price = self.parser.clean_html_tags_from_string(price).partition('R$')
            price = price.strip().split(' ')
            item['price'] = dollar_sign + ' ' + price[0]

            url = self.parser.get_single_value_from_string(raw_string=div,
                                                           xpath='//div[@class="listing-title"]//a/@href')
            item['url'] = url

            yield response.follow(url, callback=self.parse_description, cb_kwargs=item)

    def parse_description(self, response, **kwargs):
        item = kwargs
        description = self.parser.get_multiple_values_from_string(raw_string=response.text,
                                                                  xpath='//p[@class="MsoNormal"]//span/text()').strip()

        item['description'] = description

        item['category'] = self.parser.parse_category_based_on_description(description)

        yield item
