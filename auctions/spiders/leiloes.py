import scrapy
from scrapy.http import Response
import json


class LeiloesSpider(scrapy.Spider):
    name = 'leiloes'
    start_urls = ['https://www.leiloes.com.br']

    headers = {
        "Accept": "application/json, text / plain, * / *",
        "Referer": "https://www.leiloes.com.br/",
        "sec - ch - ua": 'Chromium;v="92","Not A;Brand";v="99","Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
    }

    rawheaders = {
        ":authority": "www.leiloes.com.br",
        ":method": "GET",
        ":path": "/procurar-bens?tipoBem=462&caracteristicaValor=PA:",
        ":scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "dnt": "1",
        "pragma": "no-cache",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }

    def parse(self, response: Response):
        url = 'https://www.leiloes.com.br/api/v2/lote/filtro-home?categoria=462&uf=PA&cidade=&tipo='

        request = scrapy.Request(url, callback=self.parse_api, headers=self.rawheaders)

        yield request

    def parse_api(self, response: Response):

        raw_data = response.body
        data = json.loads(raw_data)
        for item in data:
            item_id = item["id"]
            print(item_id)
