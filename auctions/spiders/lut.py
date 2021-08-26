import scrapy
from scrapy import Request

from ..utils.parser import Parser
from ..items import AuctionsItem


class LutSpider(scrapy.Spider):
    name = 'lut'
    parser = Parser()
    start_urls = ['http://www.lut.com.br/']

    def parse(self, response):
        url = f'https://www.lut.com.br/pesquisa/?txSearch={self.city}&pg=1'
        yield Request(url=url, callback=self.parse_response)

    def parse_response(self,response):
        item = AuctionsItem()
        lis = response.xpath('//li[@class="simple-card lote"]').extract()
        for li in lis:
            item['site'] = 'Lut'

            item['price'] = self.parser.get_single_value_from_string(raw_string=li,xpath='//p[@class="big"]/text()').replace('\xa0',' ')

            url = 'https://www.lut.com.br' + self.parser.get_single_value_from_string(raw_string=li,xpath='//a/@href')
            item['url'] = url

            yield response.follow(url=url, callback=self.parse_description, cb_kwargs=item)

    def parse_description(self, response, **kwargs):
        item = kwargs

        item['description'] = response.xpath('//div[@class="info-content"]/p/text()').get().strip()

        yield item

