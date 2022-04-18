# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from openpyxl import load_workbook
import os

import mysql.connector
from clients_database import  Data_base_manager


class AuctionsPipeline:
    def process_item(self, item, spider):
        # new_row_data = [
        #     [
        #         item['site'],
        #         item['category'],
        #         item['price'],
        #         item['url'],
        #         item['description']
        #     ]
        # ]
        # wb = load_workbook("results.xls")
        # # Select First Worksheet
        # ws = wb.worksheets[0]
        #
        # # Append 2 new Rows - Columns A - D
        # for row_data in new_row_data:
        #     # Append Row Values
        #     ws.append(row_data)

        print(item)
        return item
