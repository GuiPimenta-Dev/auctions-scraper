import scrapy
from ..constants.constants import GroundTypeEnum as GTEnum
from ..items import AuctionsItem
from ..utils.parser import Parser


class RochaleiloesSpider(scrapy.Spider):
    name = 'rochaleiloes'
    parser = Parser()
    id_category = {GTEnum.ALL: '0', GTEnum.RESIDENTIAL: '2', GTEnum.RURAL: '4', GTEnum.COMMERCIAL: '10'}
    start_urls = ['http://rochaleiloes.com.br/']

    def parse(self, response):
        url = f'https://rochaleiloes.com.br/busca?termos={self.city}&autos=&uf=0&cidade=&categoria={self.id_category[self.category]}&tipo=tudo&minimo=&maximo='
        yield scrapy.Request(url=url, callback=self.parse_response)

    def parse_response(self, response):
        item = AuctionsItem()
        divs = response.xpath('//div[@class="listing-item rocha-listing-lote"]').extract()
        for div in divs:
            item['site'] = 'rocha leiloes'

            price = self.parser.get_multiple_values_from_string(raw_string=div,
                                                                xpath='//ul[@class="listing-details-valores"]//li')
            _, dollar_sign, price = self.parser.clean_html_tags_from_string(price).partition('R$')
            item['price'] = dollar_sign + price

            item['url'] = self.parser.get_single_value_from_string(raw_string=div, xpath='//a/@href')

            item['description'] = self.parser.get_multiple_values_from_string(raw_string=div, xpath='//p/text()')

            yield item
