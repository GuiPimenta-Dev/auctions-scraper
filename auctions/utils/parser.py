import re
from bs4 import BeautifulSoup
from ..constants.constants import ItemsEnums


class Parser:

    def get_area_from_raw_string(self, raw_string: str, type_of_area: str) -> str:
        if type_of_area in raw_string.lower():
            return (
                re.split(type_of_area, raw_string, flags=re.IGNORECASE)[1]
                    .split('m²')[0]
                    .strip()
            )

    def get_neighborhood_from_raw_string(self, raw_string: str) -> str:
        _, _, after = raw_string.lower().partition(ItemsEnums.BAIRRO)
        return BeautifulSoup(after.strip().split(' ')[0], features="lxml").get_text(strip=True).capitalize()


    def raw_header_to_dict(self, raw_headers: str) -> dict:
        raw_headers = raw_headers.split('\n')
        raw_headers = [x.strip() for x in raw_headers if x.strip()]
        dict_header = {
            i.split(': ')[0].strip(): i.split(': ')[1].strip()
            for i in raw_headers
        }

        if 'Host' in dict_header:
            del dict_header['Host']
        if 'content-length' in dict_header:
            del dict_header['content-length']
        if 'cookie' in dict_header:
            del dict_header['cookie']
        if 'user-agent' in dict_header:
            del dict_header['user-agent']

        return dict_header
