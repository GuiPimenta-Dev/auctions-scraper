import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Response

from ..items import AuctionsItem
from ..utils.parser import Parser
from ..constants.constants import GroundTypeEnum as GTEnum


class SantacatarinaleiloesSpider(scrapy.Spider):
    name = 'santacatarinaleiloes'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "symfony=c4sfb4gb4iv4qm5dnufirac8g6; __atssc=google%3B1; __atuvc=2%7C33; __atuvs=611bc7b3453f28d9001",
        "dnt": "1",
        "Host": "www.santacatarinaleiloes.com.br",
        "Pragma": "no-cache",
        "Referer": "http://www.santacatarinaleiloes.com.br/",
        "Upgrade-Insecure-Requests": "1"
    }
    site = 'santa catarina leiloes'
    parser = Parser()
    start_urls = ['http://www.santacatarinaleiloes.com.br/lotes/index/id/18',
                  'http://www.santacatarinaleiloes.com.br/lotes/index/id/8',
                  'http://www.santacatarinaleiloes.com.br/lotes/index/id/7']

    def parse(self, response):

        if self.city == 'santa_catarina':
            item = AuctionsItem()
            item['site'] = 'Santa Catarina leilões'

            res = response.xpath('//div[@class="ds_itens_lote_ds"]').extract_first()
            try:
                res = BeautifulSoup(res,
                                    features="lxml").get_text().strip().split('\n')
            except:
                return

            for i in res:
                if 'Valor.' in i:
                    item['price'] = i.split('Valor.')[1].strip()

                elif 'Bens.' in i:
                    description = i.split('Bens.')[1].strip()
                    item['description'] = description
                    item['category'] = self.parser.parse_category_based_on_description(description)

            item['url'] = response.url

            yield item
