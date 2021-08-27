import scrapy
from ..items import AuctionsItem
from ..utils.parser import Parser


class LejeSpider(scrapy.Spider):
    name = 'leje'
    parser = Parser()

    def __init__(self, city):
        self.start_urls = [f'https://www.leje.com.br/index.php?acao=busca_rapida&keywords={city}']

    def parse(self, response):
        item = AuctionsItem()
        divs = response.xpath('//div[@class="col-lg-12 col-md-12 col-sm-12 col-xs-12 dvcs-base"]').extract()
        for div in divs:
            if self.parser.get_single_value_from_string(raw_string=div,
                                                        xpath='//div[@class="col-lg-11 col-md-10 col-sm-10 col-xs-10 dvcs-status bg-st-aberto"]/text()') == 'ABERTO PARA LANCES':
                description = self.parser.get_single_value_from_string(raw_string=div,
                                                                       xpath='//div[@class="col-lg-12 col-md-12 col-sm-12 col-xs-12 dvcs-desc"]/text()').strip()

                if self.parser.check_if_is_house(description=description):
                    item['site'] = 'Leje'

                    price_div = self.parser.get_multiple_values_from_string(raw_string=div,
                                                                            xpath='//div[@class="col-lg-12 col-md-12 col-sm-12 col-xs-12 dvcsd-in dvcsd-active"]/text()').strip()
                    _, dollar_sign, price = price_div.partition('R$')
                    price = price.strip().split('\n')[0]
                    item['price'] = dollar_sign + ' ' + price

                    id = self.parser.get_multiple_values_from_string(raw_string=div,
                                                                     xpath='//div[@class="col-lg-4 col-md-4 col-sm-4 col-xs-4 dvcsf-id"]/text()').strip()
                    id = ''.join(char for char in id if char.isdigit())
                    item['url'] = f'https://www.leje.com.br/index.php?acao=evento&cod={id}'

                    item['description'] = description

                    item['category'] = self.parser.parse_category_based_on_description(description)

                    yield item
