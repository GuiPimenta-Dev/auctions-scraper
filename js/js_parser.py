import html
import re
from unicodedata import normalize


class Parser:

    @staticmethod
    def convert_currency(amount):
        thousands_separator = "."
        currency = "R$ {:,.2f}".format(amount)
        if thousands_separator == ".":
            main_currency, fractional_currency = currency.split(".")[0], currency.split(".")[1]
            new_main_currency = main_currency.replace(",", ".")
            fractional_separator = ","
            currency = new_main_currency + fractional_separator + fractional_currency

        return currency

    @staticmethod
    def clean_html_tags_from_string(raw_string: str):
        cleanr = re.compile('<.*?>')
        return html.unescape(
            re.sub(cleanr, '', raw_string).strip().replace('\n', '').replace('\r', '').replace('\t', ''))

    @staticmethod
    def normalize_string(raw_string):
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
