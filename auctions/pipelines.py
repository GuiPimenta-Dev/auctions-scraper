# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from openpyxl import load_workbook
import os
class AuctionsPipeline:
    def process_item(self, item, spider):
        # city = 'NONE'
        # site = f"{item['site']}"
        # price = f"{item['price']}"
        # url = f"{item['url']}"
        #
        # auctions_db.insert_auction(city,site,price,url)

        print(item)
        return item
