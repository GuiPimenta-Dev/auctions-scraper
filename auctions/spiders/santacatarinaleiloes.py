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
    inicial_urls = {GTEnum.COMMERCIAL: 'http://www.santacatarinaleiloes.com.br/lotes/index/id/18',
                    GTEnum.RESIDENTIAL: 'http://www.santacatarinaleiloes.com.br/lotes/index/id/8',
                    GTEnum.RURAL: 'http://www.santacatarinaleiloes.com.br/lotes/index/id/7'}

    def __init__(self, category):
        self.start_urls = []
        if category == GTEnum.COMMERCIAL:
            self.start_urls.append(self.inicial_urls[GTEnum.COMMERCIAL])
        elif category == GTEnum.RESIDENTIAL:
            self.start_urls.append(self.inicial_urls[GTEnum.RESIDENTIAL])
        elif category == GTEnum.RURAL:
            self.start_urls.append(self.inicial_urls[GTEnum.RURAL])
        else:
            for _, value in self.inicial_urls.items():
                self.start_urls.append(value)

    def parse(self, response):

        item = AuctionsItem()
        item['site'] = 'Santa Catarina leiloes'

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
                item['description'] = i.split('Bens.')[1].strip()

        item['url'] = response.url

        yield item
