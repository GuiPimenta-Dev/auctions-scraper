import json
import sys

import requests

from base import BaseRequests


class CentralSul(BaseRequests):
    def __init__(self, city, csv_file):
        self.city = city
        self.csv_file = csv_file
        url = f"https://www.centralsuldeleiloes.com.br/api/search/auction/{self.city}"
        response = self.parse_json_response(url=url)
        self.parse(response)

    def parse(self, response):
        site = 'Central Sul'
        for body in response['body']:
            id = body['id']

            slug = body['slug']

            url = f'https://www.centralsuldeleiloes.com.br/leilao/{id}/{slug}'

            lot_url = f'https://www.centralsuldeleiloes.com.br/api/auction-detran/{id}'

            lot = self.parse_json_response(url=lot_url)['body']['lots'][0]

            price = self.convert_currency(lot['minimum_bid'])

            description = self.clean_html_tags_from_string(lot['description'])

            item = {
                'site': site,
                'price': price,
                'url': url,
                'description': description
            }

            self.write_csv(csv_file=csv_file, item=item)


if __name__ == '__main__':
    city = 'curitiba'
    # city = sys.argv[1]
    csv_file = 'teste.json'
    # csv_file = sys.argv[2]
    CentralSul(city, csv_file)

