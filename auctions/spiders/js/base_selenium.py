from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from abc import ABC, abstractmethod
from js_parser import Parser


class BaseSelenium(ABC, Parser):
    def __init__(self, url):
        chrome_options = Options()
        # chrome_options.add_argument('disable-notifications')
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url)

    @abstractmethod
    def get_url(self, city):
        pass

    @staticmethod
    def write_csv(item, csv_file):
        with open(csv_file, 'a', encoding='utf-8') as f:
            f.write(f'{item["site"]},{item["category"]},{item["price"]},{item["url"]},{item["description"]}\n')
