import scrapy
from ..items import AuctionsItem
from ..utils.parser import Parser


class KleiloesSpider(scrapy.Spider):
    name = 'kleiloes'
    parser = Parser()
    start_urls = ['https://www.kleiloes.com.br/ResultadoPesquisaCategoria.aspx?Categoria=2']

    def parse(self, response):
        item = AuctionsItem()

        trs = response.xpath('//table//tr').extract()
        trs.pop(0)
        for tr in trs:
            item['site'] = 'K Leilões'

            price = self.parser.get_single_value_from_string(raw_string=tr,
                                                             xpath='//td[3]')

            item['price'] = self.parser.clean_html_tags_from_string(price)

            url = 'https://www.kleiloes.com.br/' + self.parser.get_single_value_from_string(raw_string=tr, xpath='//a/@href')
            item['url'] = url

            yield response.follow(url=url, callback=self.parse_description, cb_kwargs=item)

    def parse_description(self, response, **kwargs):
        item = kwargs
        local = response.xpath('//div[@id="localizacao-leilao"]').get()
        if local:
            city = response.xpath('//div[@id="localizacao-leilao"]//p').extract()[-1]
            city = self.parser.clean_html_tags_from_string(city)
            if ' ' in city:
                city = city.split(' ')[0]
            if '-' in city:
                city = city.split('-')[0]

            city = self.parser.normalize_string(city)
            if city == self.city:
                description = response.xpath('//span[@id="ctl00_ContentPlaceHolder1_DescricaoCompletaSublote"]/text()').get()
                item['description'] = description

                item['category'] = self.parser.parse_category_based_on_description(description)
                yield item

