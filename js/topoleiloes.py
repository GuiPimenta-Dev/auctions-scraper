import sys
import time

from auctions.auctions.spiders.selenium.selenium_spider import SeleniumSpider


class TopoLeiloes(SeleniumSpider):

    def __init__(self, city, csv_file):
        self.csv_file = csv_file
        url = self.get_url(city)
        super().__init__(url)
        time.sleep(3)
        self.parse()

    def get_url(self, city):
        states = {'parana': {'id': '18',
                             'cities': {
                                 'antonina': '3925', 'cantagalo': '3974', 'curitiba': '4004',
                                 'fazenda_rio_grande': '4019',
                                 'goioxim': '4036', 'guaratuba': '4047', 'honorio_serpa': '4048', 'irati': '4063',
                                 'matinhos': '4126', 'paranagua': '4163', 'pinhais': '4175', 'piraquara': '4180',
                                 'pontal_do_parana': '4186', 'sao_jose_dos_pinhais': '4260', 'sertanopolis': '4275',
                                 'virmond': '4307'}
                             },
                  'santa_catarina': {
                      'id': '24',
                      'cities': {
                          'araquari': '4327', 'blumenau': '4346', 'jaragua_do_sul': '4443',
                          'timbe_do_sul': '4577'}
                  },
                  'sao_paulo': {
                      'id': '26',
                      'cities': {
                          'sao_paulo': '3828'
                      }
                  }
        }

        for state_index, state_value in states.items():
            if state_index == city:
                url = f"https://topoleiloes.com.br/busca?uf={states[state_index]['id']}&cidade=0&categoria=0"
            for city_index, city_value in state_value['cities'].items():
                if city_index == city:
                    url = f"https://topoleiloes.com.br/busca?uf={states[state_index]['id']}&cidade={city_value}&categoria=0"
        return url


    def parse(self):
        divs = self.driver.find_elements_by_xpath('//div[@class="listing-content"]')
        site = 'Topo Leilões'

        for div in divs:
            infos = div.text.split('\n')

            description = infos[1]

            if self.parser.check_if_is_house(description=description):

                category = self.parser.parse_category_based_on_description(description=description)

                _, dollar_sign, price = infos[3].partition('R$')
                price = price.strip().split(' ')[0]
                price = dollar_sign + ' ' + price

                url = div.find_element_by_xpath('//h4/a').get_attribute('href')

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
    TopoLeiloes(city, csv_file)
