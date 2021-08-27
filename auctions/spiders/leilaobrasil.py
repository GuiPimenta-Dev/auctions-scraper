import scrapy
from scrapy import FormRequest

from ..items import AuctionsItem
from ..utils.parser import Parser


class LeilaobrasilSpider(scrapy.Spider):
    name = 'leilaobrasil'
    parser = Parser()
    page = 1
    start_urls = ['https://www.leilaobrasil.com.br/buscar']

    def parse(self, response):
        crsfid = response.xpath('//input[@name="csrfid"]/@value').get()

        data = {
            'keyword': self.city,
            'csrfid': crsfid
        }

        url = 'https://www.leilaobrasil.com.br/buscar'

        yield FormRequest(url=url, formdata=data, callback=self.parse_response)

    def parse_response(self, response):
        item = AuctionsItem()
        divs = response.xpath('//div[@class="col-sm-6 col-md-4 col-lg-3 mb-4 leilao-home"]').extract()
        for div in divs:
            description = self.parser.get_single_value_from_string(raw_string=div,
                                                                   xpath='//h2[@class="h6 mb-0 text-justify"]/text()')
            if self.parser.check_if_is_house(description):
                item['site'] = 'Leilão Brasil'

                item['price'] = self.parser.get_single_value_from_string(raw_string=div,
                                                                         xpath='//h4[@class="mb-0 text-center font-weight-bold text-truncate"]/text()')

                item['url'] = 'https://www.leilaobrasil.com.br/' + self.parser.get_single_value_from_string(
                    raw_string=div, xpath='//a/@href')

                item['description'] = description

                item['category'] = self.parser.parse_category_based_on_description(description)

                yield item

        if self.page < 11:
            self.page += 1
            url = f'https://www.leilaobrasil.com.br/pagina/{self.page}'
            yield response.follow(url=url, callback=self.parse_response)
