import scrapy
from scrapy import FormRequest

from ..items import AuctionsItem
from ..utils.parser import Parser


class SatoleiloesSpider(scrapy.Spider):
    name = 'satoleiloes'
    parser = Parser()

    start_urls = ['https://www.satoleiloes.com.br']

    def parse(self, response):
        data = {
            '_method': 'POST',
            'data[onde]': 'descricao',
            'data[Bem][termo]': self.city
        }

        url = 'https://www.satoleiloes.com.br/externo/bens/pesquisaAvancada'

        yield FormRequest(url=url, formdata=data, callback=self.parse_response)

    def parse_response(self, response):
        item = AuctionsItem()
        divs = response.xpath('//div[@class="c-lote"]').extract()
        for div in divs:
            description = self.parser.get_single_value_from_string(raw_string=div,
                                                                   xpath='//div[@class="c-lote-descricao"]//a/text()')
            if self.parser.check_if_is_house(description):
                item['site'] = 'Sato Leilões'

                item['price'] = self.parser.get_single_value_from_string(raw_string=div, xpath='//big/text()')

                item['url'] = 'https://www.satoleiloes.com.br' + self.parser.get_single_value_from_string(
                    raw_string=div, xpath='//a/@href')

                item['description'] = description

                yield item

        next = response.xpath('//a[@rel="next"]/@href').get()
        if next:
            yield response.follow(url=next, callback=self.parse_response)

