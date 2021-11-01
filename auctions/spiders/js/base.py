import json
import requests
from js_parser import Parser
from scrapy import Selector


class BaseRequests(Parser):
    @staticmethod
    def parse_json_response(url: str, query_params: dict = None, headers: dict = None):
        response = requests.request('GET', url, params=query_params, headers=headers)

        return json.loads(response.text)

    @staticmethod
    def parse_html_response(url: str, query_params: dict = None, headers: dict = None):
        response = requests.request('GET', url, params=query_params, headers=headers)
        response = Selector(text=response.text)

        return response

    def write_csv(self, item, csv_file):
        with open(csv_file, 'a', encoding='utf-8') as f:
            category = self.parse_category_based_on_description(item["description"])

            item["price"] = item["price"].replace(',', '.')
            item["description"] = item['description'].replace(',', '')

            f.write(f'{item["site"]},{category},{item["price"]},{item["url"]},{item["description"]}\n')
