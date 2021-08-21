from urllib.parse import urljoin

import scrapy
from scrapy import FormRequest

from ..items import AuctionsItem
from ..utils.parser import Parser


class NakakogueleiloesSpider(scrapy.Spider):
    name = 'nakakogueleiloes'
    parser = Parser()
    start_urls = ['https://www.nakakogueleiloes.com.br/lotes/consulta/1/']

    def parse(self, response):
        data = {
            "cmp-buscar": self.city
        }
        url = 'https://www.nakakogueleiloes.com.br/lotes/consulta/1/'

        yield FormRequest(url=url, formdata=data, callback=self.parse_response)

    def parse_response(self, response):
        item = AuctionsItem()
        uls = response.xpath('//ul[@id="itemContainer"]').extract()
        for ul in uls:
            item['site'] = 'nakakogue leiloes'

            price = self.parser.get_multiple_values_from_string(raw_string=ul,
                                                                xpath='//span[3]')
            _, dollar_sign, price = self.parser.clean_html_tags_from_string(price).partition('R$')
            item['price'] = dollar_sign + price

            url = self.parser.get_single_value_from_string(raw_string=ul, xpath='//a[@class="botao"]/@href')
            item['url'] = 'https://www.nakakogueleiloes.com.br/' + url

            item['description'] = self.parser.get_multiple_values_from_string(raw_string=ul, xpath='//h3[@class="titulo-lote"]/text()')

            yield item



