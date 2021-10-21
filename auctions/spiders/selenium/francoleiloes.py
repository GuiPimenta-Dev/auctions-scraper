import time
from auctions.auctions.utils.selenium_spider import SeleniumSpider
from auctions.auctions.utils.parser import Parser


class FrancoLeiloes(SeleniumSpider):
    def __init__(self, city, csv_file):
        self.csv_file = csv_file
        url = self.get_url(city)
        super().__init__(url)
        time.sleep(3)
        self.parse()

    @staticmethod
    def parse_select(options: str):
        parser = Parser()
        options = options.split('</option>')
        cities_id = {}
        for option in options[1:-1]:
            _, _, key = option.partition('>')
            _, _, value = option.partition('value="')
            key = parser.normalize_string(key.split(' (')[0])
            value = value.split('"')[0]
            cities_id.update({key: value})
        return cities_id

    def get_url(self, city):
        alagoas_opt = """<select class="form-control listaCidadesAV grande " style="padding-left: 8px !important;font-size: 14px !important; padding-right: 8px !important; padding-left: 8px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="MACEIÓ">MACEIÓ (14)</option>
</select>"""
        bahia_opt = """<select class="form-control listaCidadesAV grande " style="padding-left: 8px !important;font-size: 14px !important; padding-right: 8px !important; padding-left: 8px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="CAMAÇARI">CAMAÇARI (6)</option>
<option value="FEIRA DE SANTANA">FEIRA DE SANTANA (9)</option>
<option value="LAURO DE FREITAS">LAURO DE FREITAS (23)</option>
<option value="MATA DE SÃO JOÃO">MATA DE SÃO JOÃO (1)</option>
<option value="SALVADOR">SALVADOR (51)</option>
</select>"""
        ceara_opt = """<select class="form-control listaCidadesAV grande " style="padding-left: 8px !important;font-size: 14px !important; padding-right: 8px !important; padding-left: 8px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="CAUCAIA">CAUCAIA (7)</option>
<option value="EUSÉBIO">EUSÉBIO (5)</option>
<option value="FORTALEZA">FORTALEZA (41)</option>
<option value="MARACANAÚ">MARACANAÚ (1)</option>
</select>"""
        df_opt = """<select class="form-control listaCidadesAV grande " style="padding-left: 8px !important;font-size: 14px !important; padding-right: 8px !important; padding-left: 8px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="ÁGUAS CLARAS">ÁGUAS CLARAS (15)</option>
<option value="BRASILIA">BRASILIA (4)</option>
<option value="BRASÍLIA">BRASÍLIA (57)</option>
<option value="SAMAMBAIA">SAMAMBAIA (4)</option>
<option value="SOBRADINHO">SOBRADINHO (3)</option>
<option value="TAGUATINGA">TAGUATINGA (6)</option>
</select>"""
        es_opt = """<select class="form-control listaCidadesAV grande " style="padding-left: 8px !important;font-size: 14px !important; padding-right: 8px !important; padding-left: 8px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="CARIACICA">CARIACICA (7)</option>
<option value="GUARAPARI">GUARAPARI (1)</option>
<option value="ITAPUÃ">ITAPUÃ (1)</option>
<option value="SERRA">SERRA (27)</option>
<option value="VILA VELHA">VILA VELHA (22)</option>
<option value="VITÓRIA">VITÓRIA (14)</option>
</select>"""
        goias_opt = """<select class="form-control listaCidadesAV grande " style="padding-left: 8px !important;font-size: 14px !important; padding-right: 8px !important; padding-left: 8px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="ANÁPOLIS">ANÁPOLIS (4)</option>
<option value="APARECIDA DE GOIÂNIA">APARECIDA DE GOIÂNIA (1)</option>
<option value="CALDAS NOVAS">CALDAS NOVAS (6)</option>
<option value="CATALÃO">CATALÃO (3)</option>
<option value="CIDADE OCIDENTAL">CIDADE OCIDENTAL (1)</option>
<option value="GOIÂNIA">GOIÂNIA (114)</option>
<option value="ITARUMÃ">ITARUMÃ (1)</option>
<option value="JATAI">JATAI (1)</option>
<option value="JATAÍ">JATAÍ (2)</option>
<option value="PLANALTINA">PLANALTINA (8)</option>
<option value="RIO VERDE">RIO VERDE (27)</option>
<option value="SAMAMBAIA">SAMAMBAIA (1)</option>
<option value="VALPARAÍSO DE GOIÁS">VALPARAÍSO DE GOIÁS (5)</option>
</select>"""
        maranhao_opt = """<select class="form-control listaCidadesAV grande " style="padding-left: 8px !important;font-size: 14px !important; padding-right: 8px !important; padding-left: 8px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="FERNANDO FALCÃO">FERNANDO FALCÃO (2)</option>
<option value="SÃO JOSÉ DE RIBAMAR">SÃO JOSÉ DE RIBAMAR (1)</option>
<option value="SÃO LUÍS">SÃO LUÍS (13)</option>
</select>"""
        minas_gerais_opt = """<select class="form-control listaCidadesAV grande " style="padding-left: 8px !important;font-size: 14px !important; padding-right: 8px !important; padding-left: 8px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="ARAÇUAÍ">ARAÇUAÍ (1)</option>
<option value="BELO HORIZONTE">BELO HORIZONTE (163)</option>
<option value="BETIM">BETIM (17)</option>
<option value="CATUTI">CATUTI (2)</option>
<option value="CONSELHEIRO LAFAIETE">CONSELHEIRO LAFAIETE (1)</option>
<option value="CONTAGEM">CONTAGEM (26)</option>
<option value="DIVINÓPOLIS">DIVINÓPOLIS (1)</option>
<option value="ESMERALDAS">ESMERALDAS (3)</option>
<option value="FORMIGA">FORMIGA (8)</option>
<option value="FRANCISCO SÁ">FRANCISCO SÁ (2)</option>
<option value="ITAJUBÁ">ITAJUBÁ (3)</option>
<option value="JUIZ DE FORA">JUIZ DE FORA (4)</option>
<option value="LAGOA SANTA">LAGOA SANTA (21)</option>
<option value="MONTES CLAROS">MONTES CLAROS (2)</option>
<option value="NOVA LIMA">NOVA LIMA (14)</option>
<option value="PASSOS">PASSOS (2)</option>
<option value="PATROCÍNIO">PATROCÍNIO (7)</option>
<option value="PEDRO LEOPOLDO">PEDRO LEOPOLDO (2)</option>
<option value="POÇOS DE CALDAS">POÇOS DE CALDAS (2)</option>
<option value="POUSO ALEGRE">POUSO ALEGRE (2)</option>
<option value="SABARÁ">SABARÁ (5)</option>
<option value="SACRAMENTO">SACRAMENTO (1)</option>
<option value="SETE LAGOAS">SETE LAGOAS (65)</option>
<option value="TEÓFILO OTONI">TEÓFILO OTONI (4)</option>
<option value="UBERABA">UBERABA (12)</option>
<option value="UBERLÂNDIA">UBERLÂNDIA (26)</option>
<option value="VARGINHA">VARGINHA (5)</option>
<option value="VÁRZEA DA PALMA">VÁRZEA DA PALMA (4)</option>
</select>"""
        mgs_opt = """<select class="form-control listaCidadesAV grande " style="padding-left: 8px !important;font-size: 14px !important; padding-right: 8px !important; padding-left: 8px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="CAMPO GRANDE">CAMPO GRANDE (32)</option>
<option value="CORUMBÁ">CORUMBÁ (1)</option>
<option value="DOURADOS">DOURADOS (4)</option>
<option value="PARANAÍBA">PARANAÍBA (2)</option>
</select>"""
        mg_opt = """<select class="form-control listaCidadesAV grande " style="padding-left: 8px !important;font-size: 14px !important; padding-right: 8px !important; padding-left: 8px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="BARRA DO GARÇAS">BARRA DO GARÇAS (8)</option>
<option value="CUIABÁ">CUIABÁ (49)</option>
<option value="RONDONÓPOLIS">RONDONÓPOLIS (2)</option>
<option value="SANTA CARMEM">SANTA CARMEM (3)</option>
<option value="STO ANTÔNIO DO LEVERGE">STO ANTÔNIO DO LEVERGE (1)</option>
<option value="VÁRZEA GRANDE">VÁRZEA GRANDE (11)</option>
</select>"""
        para_opt = """<select class="form-control listaCidadesAV grande " style="padding-left: 8px !important;font-size: 14px !important; padding-right: 8px !important; padding-left: 8px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="CASTANHAL">CASTANHAL (1)</option>
<option value="PARAUAPEBAS">PARAUAPEBAS (2)</option>
</select>"""
        paraiba_opt = """<select class="form-control listaCidadesAV grande " style="padding-left: 8px !important;font-size: 14px !important; padding-right: 8px !important; padding-left: 8px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="CABEDELO">CABEDELO (1)</option>
<option value="CAMPINA GRANDE">CAMPINA GRANDE (2)</option>
<option value="JOÃO PESSOA">JOÃO PESSOA (41)</option>
<option value="LUCENA">LUCENA (2)</option>
</select>"""
        pernambuco_opt = """<select class="form-control listaCidadesAV grande " style="padding-left: 8px !important;font-size: 14px !important; padding-right: 8px !important; padding-left: 8px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="AGRESTINA">AGRESTINA (1)</option>
<option value="GRAVATÁ">GRAVATÁ (5)</option>
<option value="JABOATÃO DOS GUARARAPES">JABOATÃO DOS GUARARAPES (4)</option>
<option value="JABOATÃO GUARARAPES">JABOATÃO GUARARAPES (1)</option>
<option value="PAULISTA">PAULISTA (2)</option>
<option value="RECIFE">RECIFE (66)</option>
</select>"""
        piaui_opt = """<select class="form-control listaCidadesAV grande " style="padding-left: 8px !important;font-size: 14px !important; padding-right: 8px !important; padding-left: 8px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="TERESINA">TERESINA (11)</option>
</select>"""
        parana_opt = """<select class="form-control listaEstadosBuscaAV " id="estadosGrandeAV" name="estadosGrandeAV" style="padding-left: 8px !important;font-size: 14px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;"><option value="0">Estado</option>
<option value="AL">AL (14)</option>
<option value="BA">BA (88)</option>
<option value="CE">CE (54)</option>
<option value="DF">DF (89)</option>
<option value="ES">ES (71)</option>
<option value="GO">GO (173)</option>
<option value="MA">MA (16)</option>
<option value="MG">MG (399)</option>
<option value="MS">MS (39)</option>
<option value="MT">MT (74)</option>
<option value="PA">PA (3)</option>
<option value="PB">PB (45)</option>
<option value="PE">PE (79)</option>
<option value="PI">PI (11)</option>
<option value="PR">PR (75)</option>
<option value="RJ">RJ (206)</option>
<option value="RN">RN (39)</option>
<option value="RS">RS (51)</option>
<option value="SC">SC (50)</option>
<option value="SE">SE (44)</option>
<option value="SP">SP (119)</option>
<option value="TO">TO (18)</option>
</select>"""
        rj_opt = """<select class="form-control listaCidadesAV grande " id="listaCidadesAV" name="listaCidadesAV" style="padding-left: 8px !important;font-size: 14px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="ANGRA DOS REIS">ANGRA DOS REIS (10)</option>
<option value="CABO FRIO">CABO FRIO (7)</option>
<option value="CAMPOS DOS GOYTACAZES">CAMPOS DOS GOYTACAZES (18)</option>
<option value="ITABORAÍ">ITABORAÍ (4)</option>
<option value="MACAÉ">MACAÉ (1)</option>
<option value="MARICÁ">MARICÁ (2)</option>
<option value="NILÓPOLIS">NILÓPOLIS (2)</option>
<option value="NITERÓI">NITERÓI (14)</option>
<option value="NOVA IGUAÇU">NOVA IGUAÇU (6)</option>
<option value="PETRÓPOLIS">PETRÓPOLIS (4)</option>
<option value="RIO DAS OSTRAS">RIO DAS OSTRAS (15)</option>
<option value="RIO DE JANEIRO">RIO DE JANEIRO (125)</option>
<option value="SÃO GONÇALO">SÃO GONÇALO (3)</option>
<option value="SÃO JOÃO DA BARRA">SÃO JOÃO DA BARRA (2)</option>
<option value="SAQUAREMA">SAQUAREMA (1)</option>
<option value="VOLTA REDONDA">VOLTA REDONDA (1)</option>
</select>"""
        rn_opt = """<select class="form-control listaCidadesAV grande " id="listaCidadesAV" name="listaCidadesAV" style="padding-left: 8px !important;font-size: 14px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="EXTREMOZ">EXTREMOZ (2)</option>
<option value="NATAL">NATAL (25)</option>
<option value="PARNAMIRIM">PARNAMIRIM (12)</option>
</select>"""
        rs_opt = """<select class="form-control listaCidadesAV grande " id="listaCidadesAV" name="listaCidadesAV" style="padding-left: 8px !important;font-size: 14px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="BAGÉ">BAGÉ (1)</option>
<option value="CACHOEIRINHA">CACHOEIRINHA (4)</option>
<option value="CANOAS">CANOAS (3)</option>
<option value="CAXIAS DO SUL">CAXIAS DO SUL (1)</option>
<option value="GRAMADO">GRAMADO (4)</option>
<option value="GRAVATAÍ">GRAVATAÍ (2)</option>
<option value="NOVO HAMBURGO">NOVO HAMBURGO (3)</option>
<option value="PANAMBI">PANAMBI (1)</option>
<option value="PORTO ALEGRE">PORTO ALEGRE (29)</option>
<option value="SÃO LEOPOLDO">SÃO LEOPOLDO (2)</option>
<option value="SAPUCAIA DO SUL">SAPUCAIA DO SUL (1)</option>
</select>"""
        sc_opt = """<select class="form-control listaCidadesAV grande " id="listaCidadesAV" name="listaCidadesAV" style="padding-left: 8px !important;font-size: 14px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="BALNEÁRIO CAMBORIÚ">BALNEÁRIO CAMBORIÚ (5)</option>
<option value="BALNEÁRIO PIÇARRAS">BALNEÁRIO PIÇARRAS (2)</option>
<option value="CAMBORIÚ">CAMBORIÚ (15)</option>
<option value="CAMPOS NOVOS">CAMPOS NOVOS (1)</option>
<option value="CRICIÚMA">CRICIÚMA (2)</option>
<option value="FLORIANÓPOLIS">FLORIANÓPOLIS (7)</option>
<option value="GAROPABA">GAROPABA (2)</option>
<option value="ITAJAÍ">ITAJAÍ (4)</option>
<option value="ITAPEMA">ITAPEMA (2)</option>
<option value="JARAGUÁ DO SUL">JARAGUÁ DO SUL (2)</option>
<option value="JOINVILLE">JOINVILLE (2)</option>
<option value="LAGES">LAGES (1)</option>
<option value="PALHOÇA">PALHOÇA (4)</option>
<option value="SÃO JOSÉ">SÃO JOSÉ (2)</option>
</select>"""
        sergipe_opt = """<select class="form-control listaCidadesAV grande " id="listaCidadesAV" name="listaCidadesAV" style="padding-left: 8px !important;font-size: 14px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="ARACAJU">ARACAJU (33)</option>
<option value="BARRA DOS COQUEIROS">BARRA DOS COQUEIROS (1)</option>
<option value="CAPELA">CAPELA (6)</option>
<option value="ITABAIANA">ITABAIANA (1)</option>
<option value="MONTE ALEGRE DE SERGIPE">MONTE ALEGRE DE SERGIPE (1)</option>
<option value="SÃO CRISTOVÃO">SÃO CRISTOVÃO (2)</option>
</select>"""
        sp_opt = """<select class="form-control listaCidadesAV grande " id="listaCidadesAV" name="listaCidadesAV" style="padding-left: 8px !important;font-size: 14px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="AGUDOS">AGUDOS (3)</option>
<option value="AVARÉ">AVARÉ (3)</option>
<option value="BAURU">BAURU (2)</option>
<option value="BOQUEIRÃO">BOQUEIRÃO (1)</option>
<option value="CAMPINAS">CAMPINAS (3)</option>
<option value="CATANDUVA">CATANDUVA (1)</option>
<option value="COTIA">COTIA (2)</option>
<option value="DIADEMA">DIADEMA (2)</option>
<option value="GUARAREMA">GUARAREMA (1)</option>
<option value="GUARUJÁ">GUARUJÁ (2)</option>
<option value="GUARULHOS">GUARULHOS (7)</option>
<option value="HORTOLÂNDIA">HORTOLÂNDIA (1)</option>
<option value="ITAPECERICA DA SERRA">ITAPECERICA DA SERRA (1)</option>
<option value="ITAPEVI">ITAPEVI (2)</option>
<option value="ITÁPOLIS">ITÁPOLIS (2)</option>
<option value="JABOTICABAL">JABOTICABAL (7)</option>
<option value="JACAREÍ">JACAREÍ (3)</option>
<option value="JUNDIAÍ">JUNDIAÍ (1)</option>
<option value="LARANJAL PAULISTA">LARANJAL PAULISTA (1)</option>
<option value="LIMEIRA">LIMEIRA (5)</option>
<option value="MACATUBA">MACATUBA (3)</option>
<option value="MAUÁ">MAUÁ (2)</option>
<option value="MORRO AGUDO">MORRO AGUDO (2)</option>
<option value="PIRATININGA">PIRATININGA (3)</option>
<option value="PRAIA GRANDE">PRAIA GRANDE (2)</option>
<option value="RANCHARIA">RANCHARIA (1)</option>
<option value="RIBEIRÃO PRETO">RIBEIRÃO PRETO (9)</option>
<option value="RIO DAS PEDRAS">RIO DAS PEDRAS (1)</option>
<option value="SANTA BÁRBARA D'OESTE">SANTA BÁRBARA D'OESTE (2)</option>
<option value="SANTO ANDRÉ">SANTO ANDRÉ (3)</option>
<option value="SANTOS">SANTOS (3)</option>
<option value="SÃO BERNARDO DO CAMPO">SÃO BERNARDO DO CAMPO (5)</option>
<option value="SÃO PAULO">SÃO PAULO (27)</option>
<option value="SOROCABA">SOROCABA (3)</option>
<option value="SUMARÉ">SUMARÉ (3)</option>
<option value="SUZANO">SUZANO (2)</option>
<option value="TIETÊ">TIETÊ (1)</option>
<option value="UBATUBA">UBATUBA (1)</option>
<option value="VINHEDO">VINHEDO (1)</option>
</select>"""
        tocantins_opt = """<select class="form-control listaCidadesAV grande " id="listaCidadesAV" name="listaCidadesAV" style="padding-left: 8px !important;font-size: 14px !important; padding-right: 3px !important; padding-left: 3px !important;max-width:158px; float:left;height: 44px;">
<option selected="selected" value="1">Todas as Cidades</option>
<option value="PALMAS">PALMAS (18)</option>
</select>"""

        alagoas_cities_id = self.parse_select(alagoas_opt)
        bahia_cities_id = self.parse_select(bahia_opt)
        ceara_cities_id = self.parse_select(ceara_opt)
        df_cities_id = self.parse_select(df_opt)
        es_cities_id = self.parse_select(es_opt)
        goias_cities_id = self.parse_select(goias_opt)
        maranhao_cities_id = self.parse_select(maranhao_opt)
        minas_gerais_cities_id = self.parse_select(minas_gerais_opt)
        mgs_cities_id = self.parse_select(mgs_opt)
        mg_cities_id = self.parse_select(mg_opt)
        para_cities_id = self.parse_select(para_opt)
        paraiba_cities_id = self.parse_select(paraiba_opt)
        pernambuco_cities_id = self.parse_select(pernambuco_opt)
        piaui_cities_id = self.parse_select(piaui_opt)
        parana_cities_id = self.parse_select(parana_opt)
        rj_cities_id = self.parse_select(rj_opt)
        rgn_cities_id = self.parse_select(rn_opt)
        rgs_cities_id = self.parse_select(rs_opt)
        sc_cities_id = self.parse_select(sc_opt)
        sergipe_cities_id = self.parse_select(sergipe_opt)
        sp_cities_id = self.parse_select(sp_opt)
        tocantins_cities_id = self.parse_select(tocantins_opt)

        states_id = {'alagoas': 'AL', 'bahia': 'BA', 'ceara': 'CE', 'distrito_federal': 'DF', 'espirito_santo': 'ES',
                     'goias': 'GO', 'maranhao': 'MA', 'minas_gerais': 'MG', 'mato_grosso_do_sul': 'MS',
                     'mato_grosso': 'MT',
                     'para': 'PA', 'paraiba': 'PB', 'pernambuco': 'PE', 'piaui': 'PI', 'parana': 'PR',
                     'rio_de_janeiro': 'RJ', 'rio_grande_do_norte': 'RN', 'rio_grande_do_sul': 'RS',
                     'santa_catarina': 'SC', 'sergipe': 'SE',
                     'sao_paulo': 'SP', 'tocantins': 'TO'}

        states_city_for_each_state = {
            states_id['alagoas']: alagoas_cities_id,
            states_id['bahia']: bahia_cities_id,
            states_id['ceara']: ceara_cities_id,
            states_id['distrito_federal']: df_cities_id,
            states_id['espirito_santo']: es_cities_id,
            states_id['goias']: goias_cities_id,
            states_id['maranhao']: maranhao_cities_id,
            states_id['mato_grosso']: mg_cities_id,
            states_id['mato_grosso_do_sul']: mgs_cities_id,
            states_id['minas_gerais']: minas_gerais_cities_id,
            states_id['para']: para_cities_id,
            states_id['paraiba']: paraiba_cities_id,
            states_id['parana']: parana_cities_id,
            states_id['pernambuco']: pernambuco_cities_id,
            states_id['piaui']: piaui_cities_id,
            states_id['rio_de_janeiro']: rj_cities_id,
            states_id['rio_grande_do_norte']: rgn_cities_id,
            states_id['rio_grande_do_sul']: rgs_cities_id,
            states_id['santa_catarina']: sc_cities_id,
            states_id['sao_paulo']: sp_cities_id,
            states_id['sergipe']: sergipe_cities_id,
            states_id['tocantins']: tocantins_cities_id,
        }

        if city in states_id:
            estado = states_id[city]
            cidade = '1'
        else:
            for state_id, state_cities in states_city_for_each_state.items():
                for city_index, city_id in state_cities.items():
                    if city_index == city:
                        estado = state_id
                        cidade = city_id

        return f'https://francoleiloes.com.br/?estado={estado}&cidade={cidade}&tipoBusca=Abertos'

    def parse(self):
        divs = self.driver.find_elements_by_xpath('//div[@class="box_inner link-leilao with-cool-menu"]')

        site = 'francoleiloes'

        urls = self.driver.find_elements_by_xpath('//*[@id="abertos"]/div/div/div')

        for div in divs:
            if div.text != '':
                infos = div.text.split('\n')

                situation = infos[0]

                if situation == 'ABERTO':
                    description = infos[6]

                    category = infos[5]

                    _, dollar_sign, price = infos[-1].partition('R$')

                    price = dollar_sign + ' ' + price

                    url = div.get_attribute('data-link')


                    item = {
                        'site': site,
                        'category': category,
                        'price': price,
                        'url': url,
                        'description': description
                    }

                    self.write_csv(item=item, csv_file=self.csv_file)




if __name__ == '__main__':
    city = 'sao_paulo'
    csv_file = 'teste.csv'
    FrancoLeiloes(city, csv_file)
