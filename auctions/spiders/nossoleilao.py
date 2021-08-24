import scrapy
from ..items import AuctionsItem
from ..utils.parser import Parser

class NossoleilaoSpider(scrapy.Spider):
    name = 'nossoleilao'
    parser = Parser()

    def __init__(self,city):
        self.start_urls = [f'https://www.nossoleilao.com.br/lotes/search?tipo=imovel&search={city}']

    def parse(self, response):
        item = AuctionsItem()
        divs = response.xpath('//div[@class="lote "]').extract()
        for div in divs:
            item['site'] = 'Nosso Leilão'

            item['price'] = self.parser.get_multiple_values_from_string(raw_string=div,xpath='//h4[@class="mb-0"]/text()').replace('\xa0', ' ')

            item['url'] = self.parser.get_single_value_from_string(raw_string=div, xpath='//a/@href')

            description = self.parser.get_single_value_from_string(raw_string=div, xpath='//div[@style="text-align: justify !important;"]')
            item['description'] = self.parser.clean_html_tags_from_string(description)

            yield item

