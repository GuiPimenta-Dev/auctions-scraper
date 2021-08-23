from scrapy.selector import Selector
import re
from unicodedata import normalize


class Parser:

    def get_multiple_values_from_string(self, raw_string: str, xpath: str):
        response = Selector(text=raw_string).xpath(xpath).extract()
        return ' '.join(response)

    def get_single_value_from_string(self, raw_string: str, xpath: str):
        return Selector(text=raw_string).xpath(xpath).get()

    def clean_html_tags_from_string(self, raw_string: str):
        cleanr = re.compile('<.*?>')
        return re.sub(cleanr, '', raw_string)

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

    def parse_select_dict(self, raw_select: str):
        opt = {}
        raw_selects = raw_select.replace('<option value=', '').replace('"', '').replace('<select>', '').replace(
            '</select>', '').strip().split('</option>')
        for select in raw_selects:
            if select:
                value, _, key = select.partition('>')
                key = self.normalize_string(key)
                opt[key] = value

        return opt

    def normalize_string(self, raw_string):
        treated_string = raw_string.lower().replace(' ', '_').replace("'", '')
        return (
            normalize('NFKD', treated_string)
            .encode('ASCII', 'ignore')
            .decode('ASCII')
        )