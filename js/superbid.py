import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from auctions.auctions.spiders.selenium.selenium_spider import SeleniumSpider


class SuperBid(SeleniumSpider):
    def __init__(self, city, csv_file):
        self.csv_file = csv_file
        url = self.get_url(city)
        super().__init__(url)
        time.sleep(3)
        self.parse()

    def get_url(self, city):
        return f'https://www.superbid.net/busca/{city}'

    def parse(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                         'path[d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"]'))).click()
        divs = self.driver.find_elements_by_xpath(
            '//div[@class="MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-justify-xs-space-between MuiGrid-grid-md-true"]')

        site = 'Super Bid'

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
    city = sys.argv[1]
    csv_file = sys.argv[2]
    SuperBid(city, csv_file)
