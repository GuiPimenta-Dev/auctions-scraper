import sys
import time

from auctions.auctions.utils.selenium_spider import SeleniumSpider


class Leiloes(SeleniumSpider):

    def __init__(self, city, csv_file):
        self.csv_file = csv_file
        url = self.get_url(city)
        super().__init__(url)
        time.sleep(10)
        self.parse()

    def get_url(self, city):
        states = {
            'rio_grande_do_sul': 'RS',
            'sao_paulo': 'SP',
            'santa_catarina': 'SC',
            'parana': 'PR',
            'para': 'PA',
            'goias': 'GO',
            'minas_gerais': 'MG',
            'rio_de_janeiro': 'RJ',
            'ceara': 'CE',
            'mato_grosso': 'MT'
        }
        if city in states:
            url = f"https://www.leiloes.com.br/procurar-bens?tipoBem=462&caracteristicaValor={states[city]}"
        else:
            url = f"https://www.leiloes.com.br/procurar-bens?tipoBem=462&caracteristicaValor={city}"

        return url

    def parse(self):
        divs = self.driver.find_elements_by_xpath('//div[@class="card not-selectable"]//a')
        for div in divs:
            site = 'Leilões'

            infos = div.text.split('\n')

            description = infos[1]

            category = self.parser.parse_category_based_on_description(description=description)

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

            self.write_csv(item=item, csv_file=self.csv_file)


if __name__ == '__main__':
    city = sys.argv[1]
    csv_file = sys.argv[2]
    Leiloes(city, csv_file)
