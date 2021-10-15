import time
from auctions.auctions.utils.selenium_spider import SeleniumSpider


class CentralSul(SeleniumSpider):
    def __init__(self, city, csv_file):
        self.csv_file = csv_file
        url = self.get_url(city)
        super().__init__(url)
        time.sleep(3)
        self.parse()

    def get_url(self, city):
        return f'https://www.centralsuldeleiloes.com.br/leilao/pesquisa?q={city}&tipo=leilao'

    def parse(self):
        trs = self.driver.find_elements_by_xpath('//table//tr')
        for tr in trs[1:]:
            site = 'CentralSul'

            description = tr.text.split('\n')[1]

            category = self.parser.parse_category_based_on_description(description=description)

            price = '-'

            url = tr.find_element_by_xpath('//td//a').get_attribute('href')

            item = {
                'site': site,
                'category': category,
                'price': price,
                'url': url,
                'description': description
            }

            self.write_csv(item=item, csv_file=self.csv_file)


if __name__ == '__main__':
    city = 'laguna'
    csv_file = 'teste.csv'
    CentralSul(city, csv_file)
