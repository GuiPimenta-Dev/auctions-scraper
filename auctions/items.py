# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AuctionsItem(scrapy.Item):
    site = scrapy.Field()
    ground_type = scrapy.Field()
    neighborhood = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    house_area = scrapy.Field()
    ground_area = scrapy.Field()
    number_of_rooms = scrapy.Field()
    garage = scrapy.Field()
    bathrooms = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()


