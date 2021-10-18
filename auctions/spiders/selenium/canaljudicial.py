import time
from auctions.auctions.utils.selenium_spider import SeleniumSpider


class CanalJudicial(SeleniumSpider):
    def __init__(self, city, csv_file):
        self.csv_file = csv_file
        url = self.get_url(city)
        super().__init__(url)
        time.sleep(5)
        self.parse()

    def get_url(self, city):
        return f'https://www.canaljudicial.com.br/busca/{city}'

    def parse(self):
        divs = self.driver.find_elements_by_xpath('//div[@class="MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-justify-xs-space-between MuiGrid-grid-md-true"]')

        site = 'Canal Judicial'

        for div in divs:
            infos = div.text.split('\n')

            description = infos[0]

            if self.parser.check_if_is_house(description=description):

                category = self.parser.parse_category_based_on_description(description=description)

                url = div.find_element_by_xpath('//p//a').get_attribute('href')

                price = infos[-2]

                item = {
                    'site': site,
                    'category': category,
                    'price': price,
                    'url': url,
                    'description': description
                }

                self.write_csv(item=item, csv_file=self.csv_file)


if __name__ == '__main__':
    city = 'curitiba'
    csv_file = 'teste.csv'
    CanalJudicial(city, csv_file)
