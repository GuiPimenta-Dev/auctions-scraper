from requests_html import AsyncHTMLSession
from abc import ABC, abstractmethod
from auctions.auctions.utils.parser import Parser


class BaseRequests(ABC):
    def __init__(self, url):
        session = AsyncHTMLSession()
        session.run(self.get_site(url, session))
        self.parser = Parser()

    async def get_site(self, url, session):
        self.response = await session.get(url)

    @abstractmethod
    def get_url(self, city):
        pass

    @staticmethod
    def write_csv(item, csv_file):
        with open(csv_file, 'a', encoding='utf-8') as f:
            f.write(f'{item["site"]},{item["category"]},{item["price"]},{item["url"]},{item["description"]}\n')
