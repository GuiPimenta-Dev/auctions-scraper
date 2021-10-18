from scrapy.selector import Selector
import re
from unicodedata import normalize


class Parser:

    def get_multiple_values_from_string(self, raw_string: str, xpath: str):
        response = Selector(text=raw_string).xpath(xpath).extract()
        return ' '.join(response).strip().replace('\n', '').replace('\r', '').replace('\t', '')

    def get_single_value_from_string(self, raw_string: str, xpath: str):
        return Selector(text=raw_string).xpath(xpath).get().strip().replace('\n', '').replace('\r', '').replace('\t',
                                                                                                                '')

    def clean_html_tags_from_string(self, raw_string: str):
        cleanr = re.compile('<.*?>')
        return re.sub(cleanr, '', raw_string).strip()

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

    def parse_select_dict(self, raw_select: str, exclude_first_option=False, split_key: str = None,
                          split_value: str = None):
        opt = {}
        raw_selects = raw_select.replace('<option value=', '').replace('"', '').replace('<select>', '').replace(
            '</select>', '').strip().split('</option>')
        if exclude_first_option:
            raw_selects = raw_selects[1:]
        for select in raw_selects:
            if select:
                value, _, key = select.partition('>')
                key = self.normalize_string(key)
                if split_key:
                    key = key.split(split_key)[0]
                if split_value:
                    value = value.split(split_value)[0]
                opt[key] = value.strip()

        return opt

    def _parse_select_dict(self, raw_select: str, exclude_first_option=False, split_key: str = None,
                           split_value: str = None
                           ):
        opt = {}
        raw_selects = raw_select.strip().split('</option>')
        if exclude_first_option:
            raw_selects = raw_selects[1:]
        for select in raw_selects:
            if select:
                _, _, after_value = select.partition(f'{split_value}="')
                value = after_value.split('"')[0]
                key, _, _ = select.partition(f'{split_key}')
                key = key.split('>')[-1]

                try:
                    key = key.split('-')[0].strip()
                except:
                    pass
                key = self.normalize_string(key)
                opt[key] = value.strip()
        try:
            del opt['']
        except:
            pass
        return opt

    def parse_select_dict_without_values(self, raw_select: str):
        opt = []
        options = raw_select.split('</option>')[1:]
        for option in options:
            cleaned_option = self.clean_html_tags_from_string(option.strip())
            if cleaned_option:
                opt.append(cleaned_option)

        return opt

    def normalize_string(self, raw_string):
        treated_string = raw_string.lower().replace(' ', '_').replace("'", '')
        return (
            normalize('NFKD', treated_string)
                .encode('ASCII', 'ignore')
                .decode('ASCII')
        )

    @staticmethod
    def parse_category_based_on_description(description):  # sourcery no-metrics
        under_description = description.lower()
        if 'flat' in under_description:
            return 'Flat'
        elif 'duplex' in under_description:
            return 'Duplex'
        elif 'trilex' in under_description:
            return 'Triplex'
        elif 'studio' in under_description:
            return 'Studio'
        elif 'kitinete' in under_description or 'conjugado' in under_description:
            return 'Kitinete'
        elif 'créditos imobiliários' in under_description:
            return 'Créditos imobiliários'
        elif 'massa falida' in under_description:
            return 'Massa Falida'
        elif 'sobrado' in under_description:
            return 'Sobrado'
        elif 'chácara' in under_description or 'chacara' in under_description:
            return 'Chácara'
        elif 'fazenda' in under_description:
            return 'Fazenda'
        elif 'sítio' in under_description or 'sitio' in under_description:
            return 'Sítio'
        elif 'barracão' in under_description or 'barracao' in under_description:
            return 'Barracão'
        elif 'galpão' in under_description or 'galpao' in under_description:
            return 'Galpão'
        elif 'depósito' in under_description:
            return 'Depósito'
        elif 'armazém' in under_description:
            return 'Armazém'
        elif 'box' in under_description:
            return 'Box'
        elif 'loja' in under_description:
            return 'Loja'
        elif 'sala comercial' in under_description:
            return 'Sala comercial'
        elif 'edifício comercial' in under_description or 'prédio comercial' in under_description:
            return 'Edifício comercial'
        elif 'edifício residencial' in under_description or 'prédio residencial' in under_description:
            return 'Edifício residencial'
        elif 'casa' in under_description:
            return 'Casa'
        elif 'apartamento' in under_description or 'apto' in under_description or 'ap.' in under_description:
            return 'Apartamento'
        elif 'condomínio' in under_description or 'cond.' in under_description:
            return 'Condomínio'
        elif 'garagem' in under_description:
            return 'Garagem'
        elif 'terreno' in under_description or 'terr.' in under_description:
            return 'Terreno'
        elif 'lote' in under_description:
            return 'Lote'
        elif 'residencial' in under_description:
            return 'Residencial'
        elif 'comercial' in under_description:
            return 'Comercial'
        elif 'rural' in under_description:
            return 'Rural'
        elif 'prédio' in under_description or 'predio' in under_description or 'edifício' in under_description or 'edificação' in under_description:
            return 'Prédio'
        elif 'imóvel' in under_description:
            return 'Imóvel'
        else:
            return 'Não Identificado'

    @staticmethod
    def check_if_is_house(description: str):  # sourcery no-metrics
        under_description = description.lower()
        if 'flat' in under_description:
            return True
        elif 'duplex' in under_description:
            return True
        elif 'trilex' in under_description:
            return True
        elif 'studio' in under_description:
            return True
        elif 'kitinete' in under_description or 'conjugado' in under_description:
            return True
        elif 'créditos imobiliários' in under_description:
            return True
        elif 'massa falida' in under_description:
            return True
        elif 'sobrado' in under_description:
            return True
        elif 'chácara' in under_description or 'chacara' in under_description:
            return True
        elif 'fazenda' in under_description:
            return True
        elif 'sítio' in under_description or 'sitio' in under_description:
            return True
        elif 'barracão' in under_description or 'barracao' in under_description:
            return True
        elif 'galpão' in under_description or 'galpao' in under_description:
            return True
        elif 'depósito' in under_description:
            return True
        elif 'armazém' in under_description:
            return True
        elif 'box' in under_description:
            return True
        elif 'loja' in under_description:
            return True
        elif 'sala comercial' in under_description:
            return True
        elif 'edifício comercial' in under_description or 'prédio comercial' in under_description:
            return True
        elif 'edifício residencial' in under_description or 'prédio residencial' in under_description:
            return True
        elif 'casa' in under_description:
            return True
        elif 'apartamento' in under_description or 'apto' in under_description or 'ap.' in under_description:
            return True
        elif 'condomínio' in under_description or 'cond.' in under_description:
            return True
        elif 'garagem' in under_description:
            return True
        elif 'terreno' in under_description or 'terr.' in under_description:
            return True
        elif 'lote' in under_description:
            return True
        elif 'residencial' in under_description:
            return True
        elif 'comercial' in under_description:
            return True
        elif 'rural' in under_description:
            return True
        elif 'prédio' in under_description or 'predio' in under_description or 'edifício' in under_description or 'edificação' in under_description:
            return True
        elif 'imóvel' in under_description:
            return True
        else:
            return False

