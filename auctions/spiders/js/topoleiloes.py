import sys

from scrapy import Selector

from base import BaseRequests


class TopoLeiloes(BaseRequests):

    def __init__(self, city, csv_file):
        self.csv_file = csv_file

        for category in ['4', '6', '12']:
            url = self.parse_url(city, category)
            response = self.parse_html_response(url=url)
            self.parse(response)

    def parse_url(self, city, category):
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

        url = ''

        for state_index, state_value in states.items():
            if state_index == city:
                url = f"https://topoleiloes.com.br/busca?uf={states[state_index]['id']}&cidade=0&categoria={category}"
            for city_index, city_value in state_value['cities'].items():
                if city_index == city:
                    url = f"https://topoleiloes.com.br/busca?uf={states[state_index]['id']}&cidade={city_value}&categoria={category}"

        return url

    def parse(self, response):
        divs = response.xpath('//div[@class="listing-item evo-pix-box"]').extract()
        site = 'Topo Leilões'

        for div in divs:
            div = Selector(text=div)

            description = self.clean_html_tags_from_string(div.xpath('//h4/a/@title').get())

            _, dollar_sign, price = div.xpath('//ul[@class="listing-details-valores"]/li').get().partition('R$')
            price = self.clean_html_tags_from_string(price.strip().split(' ')[0])
            price = dollar_sign + ' ' + price

            url = div.xpath('//a[@class="details button border btn-detalhes"]/@href').get()

            item = {
                'site': site,
                'price': price,
                'url': url,
                'description': description
            }

            self.write_csv(csv_file=csv_file, item=item)


if __name__ == '__main__':
    city = sys.argv[1]
    csv_file = sys.argv[2]
    TopoLeiloes(city, csv_file)
