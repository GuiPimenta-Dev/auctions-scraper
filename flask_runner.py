import datetime
import logging
import os
from threading import *
import pandas as pd
import json

from auctions.utils.parser import Parser


class JSApp():
    def __init__(self, spider, city, result_csv):
        super().__init__()
        self.spider = spider
        self.city = city
        self.result_csv = result_csv

    def run(self):
        os.system(
            f'python C:\\Users\\gabriel\\auctions\\auctions\\spiders\\js\\{self.spider}.py "{self.city}" "{self.result_csv}.csv"')


class App():
    def __init__(self, spider, city, result_csv):
        super().__init__()
        self.spider = spider
        self.city = city
        self.result_csv = result_csv


class Runner:

    def run_robots(self, city):
        parser = Parser()
        city = parser.normalize_string(city)
        result_csv = 'output/' + city + '-' + datetime.datetime.now().strftime('%H_%M_%S')

        # spider_list_scrapy = ['amleiloeiro', 'biasleiloes', 'freitasleiloeiro', 'joaoluizleiloes', 'kleiloes',
        #                       'kronbergleiloes', 'lancenoleilao', 'leilaobrasil', 'leilaovip',
        #                       'leiloesjudiciais', 'leje', 'lut', 'megaleiloes', 'milanleiloes', 'nakakogueleiloes',
        #                       'nossoleilao', 'psnleiloes', 'rochaleiloes', 'santacatarinaleiloes',
        #                       'satoleiloes', 'sodresantoro', 'topoleiloes', 'zukerman']
        #
        # spider_list_selenium = [ 'francoleiloes','canaljudicial', 'centralsul',
        #                         'superbid', 'caixa', 'resale']

        spider_list_scrapy = [ 'zukerman' ]

        for spider in spider_list_scrapy:
            os.system(f'scrapy crawl {spider} -a city="{city}" -o {result_csv}.csv')

        # for spider in spider_list_selenium:
        #     os.system(f'python C:\\Users\\gabriel\\auctions\\auctions\\spiders\\js\\{spider}.py "{city}" "{result_csv}.csv"')

        read_file = pd.read_csv(f'./{result_csv}.csv', names=['site', 'category', 'price', 'url', 'description'])
        return json.loads(read_file.to_json(orient='table', index=False))


