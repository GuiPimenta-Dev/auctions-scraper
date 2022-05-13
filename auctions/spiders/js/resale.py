import json
import sys

import requests

from base import BaseRequests
from auctions.utils.parser import Parser
parser = Parser()

class Resale(BaseRequests):
    def __init__(self, city, csv_file):
        self.csv_file = csv_file
        self.city = city.replace('_', '-').title()
        self.headers = {"x-api-key": "TFqvYJxuhO67Bo5WOzspQ6UENhuIZFVvrhLIcCig"}

        houses = self.get_response(city)
        if houses:
            self.parse(houses)

    def get_response(self, city):
        city = self.get_city_slug(city)
        if city:
            return self.get_cities(city)

    def get_city_slug(self, chosen_city):
        url = "https://q3jhhgksa9.execute-api.us-east-2.amazonaws.com/prod/city"

        cities = self.parse_json_response(url=url, headers=self.headers)
        for city in cities:
            normalized_city = self.normalize_string(city['name'])
            if normalized_city == chosen_city:
                return city['slug']

    def get_cities(self, city):
        url = "https://q3jhhgksa9.execute-api.us-east-2.amazonaws.com/prod/property"

        querystring = {"search": city, "valor-max": "70000000", "order": "data"}

        response = self.parse_json_response(url=url, query_params=querystring, headers=self.headers)

        return response['data']

    def parse(self, houses):
        site = 'Resale'
        for house in houses:
            bedrooms = house['caracteristicas']['dormitorios']
            house_id = house['tags'][0]

            description = self.clean_html_tags_from_string(house['descricao'].replace('.\xa0', ''))

            category = house['tipo_imovel'].replace(',', '')

            price = self.convert_currency(house['valores']['valor_venda']).replace(',', '.')

            url = f'https://www.resale.com.br/imovel/{self.city}/{bedrooms}-Quartos/{house_id}'

            item = {
                'site': site,
                'category': category,
                'price': price,
                'url': url,
                'description': description
            }
            print(item)
            with open(self.csv_file, 'a', encoding='utf-8') as f:

                f.write(f'{item["site"]},{item["category"]},{item["price"]},{item["url"]},{item["description"]}\n')


if __name__ == '__main__':
    city = sys.argv[1]
    csv_file = sys.argv[2]
    Resale(city, csv_file)
