from scrapy.selector import Selector
import re


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
