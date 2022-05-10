import sys
import time

from base_selenium import BaseSelenium
from auctions.utils.parser import Parser
parser = Parser()

class Leiloes(BaseSelenium):

    def __init__(self, city, csv_file):
        self.csv_file = csv_file
        self.city = city
        url = self.get_url(city)
        super().__init__(url)
        time.sleep(10)
        self.parse()

    def get_url(self, city):

        states_id, _ = self.get_states_id()

        if city in states_id:
            url = f"https://www.leiloes.com.br/procurar-bens?tipoBem=462&caracteristicaValor={states_id[city]}"
        else:
            url = f"https://www.leiloes.com.br/procurar-bens?tipoBem=462&caracteristicaValor={city}"

        return url

    def parse(self):
        divs = self.driver.find_elements_by_xpath('//div[@class="card not-selectable"]//a')
        site = 'Leilões'

        for div in divs:
            infos = div.text.split('\n')

            description = infos[1]

            category = self.parse_category_based_on_description(description=description)

            _, dollar_sign, price = infos[2].partition('R$')
            price = dollar_sign + price

            url = div.get_attribute('href')

            item = {
                'site': site,
                'category': category,
                'price': price,
                'url': url,
                'description': description
            }

            if self.city in parser.normalize_string(item['description']) or self.city in parser.normalize_string(
                    item['url']):
                self.write_csv(csv_file=csv_file, item=item)


if __name__ == '__main__':
    city = sys.argv[1]
    csv_file = sys.argv[2]
    Leiloes(city, csv_file)