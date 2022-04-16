import datetime
import logging
import os
from threading import *
import teste as pd
import json

from auctions.utils.parser import Parser


class JSApp(Thread):
    def __init__(self, spider, city, result_csv):
        super().__init__()
        self.spider = spider
        self.city = city
        self.result_csv = result_csv

    def run(self):
        os.system(
            f'python C:\\Users\\gabriel\\auctions\\auctions\\spiders\\js\\{self.spider}.py "{self.city}" "{self.result_csv}.csv"')


class App(Thread):
    def __init__(self, spider, city, result_csv):
        super().__init__()
        self.spider = spider
        self.city = city
        self.result_csv = result_csv

    def run(self):
        os.system(f'scrapy crawl {self.spider} -a city="{self.city}" -o {self.result_csv}.csv')


class Runner:

    def run_robots(self, city):
        parser = Parser()
        city = parser.normalize_string(city)
        result_csv = 'output/' + city + '-' + datetime.datetime.now().strftime('%H_%M_%S')

        app1 = App(spider='amleiloeiro', city=city, result_csv=result_csv)
        app2 = App(spider='biasleiloes', city=city, result_csv=result_csv)
        app3 = App(spider='freitasleiloeiro', city=city, result_csv=result_csv)
        app4 = App(spider='joaoluizleiloes', city=city, result_csv=result_csv)
        app5 = App(spider='kleiloes', city=city, result_csv=result_csv)
        app6 = App(spider='kronbergleiloes', city=city, result_csv=result_csv)
        app7 = App(spider='lancenoleilao', city=city, result_csv=result_csv)
        app8 = App(spider='leilaobrasil', city=city, result_csv=result_csv)
        app9 = App(spider='leilaovip', city=city, result_csv=result_csv)
        app10 = App(spider='leiloesjudiciais', city=city, result_csv=result_csv)
        app11 = App(spider='leje', city=city, result_csv=result_csv)
        app12 = App(spider='lut', city=city, result_csv=result_csv)
        app13 = App(spider='megaleiloes', city=city, result_csv=result_csv)
        app14 = App(spider='milanleiloes', city=city, result_csv=result_csv)
        app15 = App(spider='nakakogueleiloes', city=city, result_csv=result_csv)
        app16 = App(spider='nossoleilao', city=city, result_csv=result_csv)
        app17 = App(spider='psnleiloes', city=city, result_csv=result_csv)
        app18 = App(spider='rochaleiloes', city=city, result_csv=result_csv)
        app19 = App(spider='santacatarinaleiloes', city=city, result_csv=result_csv)
        app20 = App(spider='satoleiloes', city=city, result_csv=result_csv)
        app21 = App(spider='sodresantoro', city=city, result_csv=result_csv)
        app22 = App(spider='topoleiloes', city=city, result_csv=result_csv)
        app23 = App(spider='zukerman', city=city, result_csv=result_csv)

        app24 = JSApp(spider='canaljudicial', city=city, result_csv=result_csv)
        app26 = JSApp(spider='centralsul', city=city, result_csv=result_csv)
        app27 = JSApp(spider='francoleiloes', city=city, result_csv=result_csv)
        app28 = JSApp(spider='superbid', city=city, result_csv=result_csv)
        app29 = JSApp(spider='topoleiloes', city=city, result_csv=result_csv)
        app30 = JSApp(spider='caixa', city=city, result_csv=result_csv)
        app31 = JSApp(spider='resale', city=city, result_csv=result_csv)

        app1.run()
        app2.run()
        app3.run()
        app4.run()
        app5.run()
        app6.run()
        app7.run()
        app8.run()
        app9.run()
        app10.run()
        app11.run()
        app12.run()
        app13.run()
        app14.run()
        app15.run()
        app16.run()
        app17.run()
        app18.run()
        app19.run()
        app20.run()
        app21.run()
        app22.run()
        app23.run()
        app24.run()
        app26.run()
        app27.run()
        app28.run()
        app29.run()
        app30.run()
        app31.run()

        app1.start()
        app2.start()
        app3.start()
        app4.start()
        app5.start()
        app6.start()
        app7.start()
        app8.start()
        app9.start()
        app10.start()
        app11.start()
        app12.start()
        app13.start()
        app14.start()
        app15.start()
        app16.start()
        app17.start()
        app18.start()
        app19.start()
        app20.start()
        app21.start()
        app22.start()
        app23.start()
        app24.start()
        app26.start()
        app27.start()
        app28.start()
        app29.start()
        app30.start()
        app31.start()

        app1.join()
        app2.join()
        app3.join()
        app4.join()
        app5.join()
        app6.join()
        app7.join()
        app8.join()
        app9.join()
        app10.join()
        app11.join()
        app12.join()
        app13.join()
        app14.join()
        app15.join()
        app16.join()
        app17.join()
        app18.join()
        app19.join()
        app20.join()
        app21.join()
        app22.join()
        app23.join()
        app24.join()
        app26.join()
        app27.join()
        app28.join()
        app29.join()
        app30.join()
        app31.join()

        read_file = pd.read_csv(f'./{result_csv}.csv', names=['site', 'category', 'price', 'url', 'description'])
        return json.loads(read_file.to_json(orient='table', index=False))
