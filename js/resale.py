import json
import sys

import requests

from auctions.auctions.utils.parser import Parser


class Resale:
    def __init__(self, city, csv_file):
        self.csv_file = csv_file
        self.city = city.replace('_', '-').title()
        houses = self.get_url(city)
        self.parse(houses)

    @staticmethod
    def get_city_slug(chosen_city):
        parser = Parser()
        url = "https://q3jhhgksa9.execute-api.us-east-2.amazonaws.com/prod/city"

        payload = ""
        headers = {"x-api-key": "TFqvYJxuhO67Bo5WOzspQ6UENhuIZFVvrhLIcCig"}
        response = requests.request("GET", url, data=payload, headers=headers)
        cities = json.loads(response.text)
        for city in cities:
            normalized_city = parser.normalize_string(city['name'])
            if normalized_city == chosen_city:
                return city['slug']

    @staticmethod
    def get_cities(city):
        import requests

        url = "https://q3jhhgksa9.execute-api.us-east-2.amazonaws.com/prod/property"

        querystring = {"search": city, "valor-max": "70000000", "order": "data"}

        payload = ""
        headers = {"x-api-key": "TFqvYJxuhO67Bo5WOzspQ6UENhuIZFVvrhLIcCig"}

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        return json.loads(response.text)['data']

    @staticmethod
    def get_url(city):
        city = Resale.get_city_slug(city)
        return Resale.get_cities(city)

    def parse(self, houses):
        site = 'Resale'
        for house in houses:
            bedrooms = house['caracteristicas']['dormitorios']
            house_id = house['tags'][0]
            description = house['descricao'].replace('\n', '').replace('\r', ' ')
            category = house['tipo_imovel']
            price = Resale.convert_currency(house['valores']['valor_venda'])
            if '394.902,00' in price:
                u = 1
            url = f'https://www.resale.com.br/imovel/{self.city}/{bedrooms}-Quartos/{house_id}'
            item = {
                'site': site,
                'category': category,
                'price': price,
                'url': url,
                'description': description
            }
            with open(self.csv_file, 'a', encoding='utf-8') as f:
                f.write(f'{item["site"]},{item["category"]},{item["price"]},{item["url"]},{item["description"]}\n')

    @staticmethod
    def convert_currency(amount):
        thousands_separator = "."
        currency = "R$ {:,.2f}".format(amount)
        if thousands_separator == ".":
            main_currency, fractional_currency = currency.split(".")[0], currency.split(".")[1]
            new_main_currency = main_currency.replace(",", ".")
            fractional_separator = ","
            currency = new_main_currency + fractional_separator + fractional_currency

        return currency


if __name__ == '__main__':
    city = sys.argv[1]
    csv_file = sys.argv[2]
    Resale(city, csv_file)
