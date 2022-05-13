from auctions.utils.parser import Parser

parser = Parser()


class AuctionsPipeline:
    def process_item(self, item, spider):
        if spider.city in parser.normalize_string(item['description']) or spider.city in parser.normalize_string(
                item['url']):
            return item
