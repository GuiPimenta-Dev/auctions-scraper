import datetime
import os
from threading import *
import os
import glob
import csv
import pandas as pd
from xlsxwriter.workbook import Workbook


class App(Thread):
    def __init__(self, spider, city, result_csv):
        super().__init__()
        self.spider = spider
        self.city = city
        self.result_csv = result_csv

    def run(self):
        os.system(f'scrapy crawl {self.spider} -a city="{self.city}" -o {self.result_csv}.csv')


if __name__ == '__main__':
    city = 'curitiba'
    result_csv = city + '-' + datetime.datetime.now().strftime('%H_%M_%S')

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

    read_file = pd.read_csv(f'./{result_csv}.csv')
    read_file.to_excel(f'./{result_csv}.xlsx', index=None, header=['Site', 'Categoria', 'Preço', 'Url', 'Descrição'])
    os.system(f"start EXCEL.EXE ./{result_csv}.xlsx")

