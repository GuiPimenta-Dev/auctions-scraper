import scrapy
from ..items import AuctionsItem
from ..utils.parser import Parser


class JoaoluizleiloesSpider(scrapy.Spider):
    name = 'joaoluizleiloes'
    parser = Parser()

    def __init__(self, city):
        self.start_urls = [f'http://joaoluizleiloes.com.br/lotes/search?search={city}']

    def parse(self, response):
        item = AuctionsItem()
        divs = response.xpath('//div[@class="card-body"]').extract()
        for div in divs:
            item['site'] = 'João Luiz Leilões'

            item['price'] = self.parser.get_single_value_from_string(raw_string=div,
                                                                     xpath='//h4[@class="mb-0"]/text()').replace('\xa0',
                                                                                                                 ' ')

            item['url'] = self.parser.get_single_value_from_string(raw_string=div, xpath='//a/@href')


            description = self.parser.get_single_value_from_string(raw_string=div, xpath='//h5/text()')
            item['description'] = description

            item['category'] = self.parser.parse_category_based_on_description(description)

            yield item
