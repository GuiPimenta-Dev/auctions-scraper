import time
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_selenium import BaseSelenium
from auctions.utils.parser import Parser

parser = Parser()
class SuperBid(BaseSelenium):
    def __init__(self, city, csv_file):
        self.csv_file = csv_file
        url = self.get_url(city)
        super().__init__(url)
        time.sleep(3)
        self.city = city
        self.parse()

    def get_url(self, city):
        return f'https://www.superbid.net/busca/{city}'

    def parse(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                         'path[d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"]'))).click()

        site = 'Super Bid'
        divs = self.driver.find_elements_by_xpath(
            '//div[@class="MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-justify-xs-space-between MuiGrid-grid-md-true"]')
        for div in divs:
            description = div.text
            print(description)
            category = self.parse_category_based_on_description(description=description)

            price = div.find_element_by_xpath('//div/span[@class="jss3941 jss3946"]')

            url = self.driver.find_element_by_xpath('//p[@class="MuiTypography-root jss3936 MuiTypography-body1"]/a').get_attribute('href')

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
    SuperBid(city, csv_file)