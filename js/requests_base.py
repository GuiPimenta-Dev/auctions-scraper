import json
import requests
from my_parser import Parser


class BaseRequests(Parser):
    @staticmethod
    def parse_request(url):
        payload = ""
        response = requests.request("GET", url, data=payload)

        return json.loads(response.text)

    def write_csv(self, item, csv_file):
        with open(csv_file, 'a', encoding='utf-8') as f:
            category = self.parse_category_based_on_description(item["description"])

            f.write(f'{item["site"]},{category},{item["price"]},{item["url"]},{item["description"]}\n')
