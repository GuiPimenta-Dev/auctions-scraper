import scrapy
from scrapy import Request

from ..items import AuctionsItem
from ..utils.parser import Parser
from ..constants.constants import GroundTypeEnum as GTEnum


class LeilaovipSpider(scrapy.Spider):
    name = 'leilaovip'
    parser = Parser()
    states_opt = """<select name="ctl00$Holder$ctl00$drpEstadoCod" onchange="javascript:setTimeout('__doPostBack(\'ctl00$Holder$ctl00$drpEstadoCod\',\'\')', 0)" id="Holder_ctl00_drpEstadoCod" class="form-control form-control-lg color-pesquisa font-md">
		<option selected="selected" value="0">ESTADO</option>
		<option value="28">AMAZONAS</option>
		<option value="25">BAHIA</option>
		<option value="24">DISTRITO FEDERAL</option>
		<option value="14">GOIÁS</option>
		<option value="12">MARANHÃO</option>
		<option value="22">MATO GROSSO</option>
		<option value="18">MINAS GERAIS</option>
		<option value="9">PARÁ</option>
		<option value="3">PARAÍBA</option>
		<option value="10">PARANÁ</option>
		<option value="16">PERNAMBUCO</option>
		<option value="21">PIAUÍ</option>
		<option value="7">RIO DE JANEIRO</option>
		<option value="23">RIO GRANDE DO NORTE</option>
		<option value="8">RIO GRANDE DO SUL</option>
		<option value="15">RORAIMA</option>
		<option value="5">SANTA CATARINA</option>
		<option value="13">SÃO PAULO</option>
		<option value="19">SERGIPE</option>
	</select>"""
    amazonas_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="173">PAUINI</option>

</select>"""
    bahia_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="242">BARREIRAS</option>
	<option value="282">CANDEIAS</option>
	<option value="335">FEIRA DE SANTANA</option>
	<option value="434">LAPAO</option>
	<option value="435">LAURO DE FREITAS</option>
	<option value="547">SANTA MARIA DA VITORIA</option>
	<option value="592">TEIXEIRA DE FREITAS</option>
	<option value="609">VALENCA</option>

</select>"""
    df_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="806">BRASILIA</option>

</select>"""
    goias_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="871">CIDADE OCIDENTAL</option>
	<option value="901">GOIANIA</option>
	<option value="949">MINACU</option>
	<option value="950">MINEIROS</option>

</select>"""
    maranhao_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="1142">IMPERATRIZ</option>
	<option value="1182">PAÇO DO LUMIAR</option>
	<option value="1236">SAO JOSE DE RIBAMAR</option>
	<option value="1238">SÃO LUÍS</option>

</select>"""
    mg_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="2300">PRIMAVERA DO LESTE</option>

</select>"""
    minas_gerais_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="1301">ANTONIO CARLOS</option>
	<option value="1323">BAEPENDI</option>
	<option value="1335">BELO HORIZONTE</option>
	<option value="1439">CATUTI</option>
	<option value="1517">DIVINOPOLIS</option>
	<option value="1595">GUAXUPE</option>
	<option value="1637">ITAJUBA</option>
	<option value="1663">JACUTINGA</option>
	<option value="1676">JEQUITINHONHA</option>
	<option value="2106">VARZEA DA PALMA</option>

</select>"""
    para_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="2458">SAO GERALDO DO ARAGUAIA</option>

</select>"""
    paraiba_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="2458">SAO GERALDO DO ARAGUAIA</option>

</select>"""
    parana_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="3300">LONDRINA</option>
	<option value="3371">PEROLA</option>
	<option value="3374">PINHAIS</option>
	<option value="3496">UMUARAMA</option>

</select>"""
    pernambuco_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="2790">JABOATAO DOS GUARARAPES</option>

</select>"""
    piaui_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="3036">PARNAIBA</option>

</select>"""
    rj_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="3520">CACHOEIRAS DE MACACU</option>
	<option value="3544">MACAÉ</option>
	<option value="3554">NILOPOLIS</option>
	<option value="3556">NOVA FRIBURGO</option>
	<option value="3557">NOVA IGUACU</option>
	<option value="3575">RIO DE JANEIRO</option>
	<option value="3580">SAO GONCALO</option>

</select>"""
    rgn_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="3654">JANDAIRA</option>

</select>"""
    rgs_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="3908">CANOAS</option>
	<option value="4120">OSORIO</option>
	<option value="4154">PORTO ALEGRE</option>

</select>"""
    roraima_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="3819">CARACARAI</option>

</select>"""
    sc_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="4413">FLORIANOPOLIS</option>
	<option value="4434">ICARA</option>
	<option value="4454">ITAPOA</option>
	<option value="4462">JOINVILLE</option>
	<option value="4549">SALETE</option>

</select>"""
    sp_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="4726">ARACOIABA DA SERRA</option>
	<option value="4731">ARARAS</option>
	<option value="4789">CABREUVA</option>
	<option value="4802">CAMPINAS</option>
	<option value="4837">COSMOPOLIS</option>
	<option value="4844">CUBATAO</option>
	<option value="4862">EMBU DAS ARTES</option>
	<option value="4907">GUARUJA</option>
	<option value="4908">GUARULHOS</option>
	<option value="4931">INDAIATUBA</option>
	<option value="4945">ITAI</option>
	<option value="4948">ITANHAEM</option>
	<option value="4950">ITAPECERICA DA SERRA</option>
	<option value="4958">ITAPUI</option>
	<option value="4963">ITATIBA</option>
	<option value="4972">JABOTICABAL</option>
	<option value="4997">LEME</option>
	<option value="5039">MOGI DAS CRUZES</option>
	<option value="5044">MONGAGUA</option>
	<option value="5083">OSASCO</option>
	<option value="5119">PERUIBE</option>
	<option value="5129">PIRACICABA</option>
	<option value="5183">RIBEIRAO PRETO</option>
	<option value="5219">SANTA ISABEL</option>
	<option value="5230">SANTO ANDRE</option>
	<option value="5238">SANTOS</option>
	<option value="5240">SÃO BERNARDO DO CAMPO</option>
	<option value="5241">SAO CAETANO DO SUL</option>
	<option value="5252">SAO JOSE DO RIO PRETO</option>
	<option value="5253">SAO JOSE DOS CAMPOS</option>
	<option value="5258">SÃO PAULO</option>
	<option value="5259">SAO PEDRO</option>
	<option value="5261">SAO ROQUE</option>
	<option value="5299">TATUI</option>
	<option value="5329">VARGEM GRANDE PAULISTA</option>

</select>"""
    sergipe_opt = """<select name="ctl00$Holder$ctl00$drpCidadeCod" id="Holder_ctl00_drpCidadeCod" class="form-control form-control-lg color-pesquisa font-md">
	<option value="0"></option>
	<option value="4621">ARACAJU</option>

</select>"""

    states_id = parser.parse_select_dict(raw_select=states_opt, exclude_first_option=True)
    amazonas_cities_id = parser.parse_select_dict(raw_select=amazonas_opt, exclude_first_option=True)
    bahia_cities_id = parser.parse_select_dict(raw_select=bahia_opt, exclude_first_option=True)
    df_cities_id = parser.parse_select_dict(raw_select=df_opt, exclude_first_option=True)
    goias_cities_id = parser.parse_select_dict(raw_select=goias_opt, exclude_first_option=True)
    maranhao_cities_id = parser.parse_select_dict(raw_select=maranhao_opt, exclude_first_option=True)
    mg_cities_id = parser.parse_select_dict(raw_select=mg_opt, exclude_first_option=True)
    minas_gerais_cities_id = parser.parse_select_dict(raw_select=minas_gerais_opt, exclude_first_option=True)
    para_cities_id = parser.parse_select_dict(raw_select=para_opt, exclude_first_option=True)
    paraiba_cities_id = parser.parse_select_dict(raw_select=paraiba_opt, exclude_first_option=True)
    parana_cities_id = parser.parse_select_dict(raw_select=parana_opt, exclude_first_option=True)
    pernambuco_cities_id = parser.parse_select_dict(raw_select=pernambuco_opt, exclude_first_option=True)
    piaui_cities_id = parser.parse_select_dict(raw_select=piaui_opt, exclude_first_option=True)
    rj_cities_id = parser.parse_select_dict(raw_select=rj_opt, exclude_first_option=True)
    rgn_cities_id = parser.parse_select_dict(raw_select=rgn_opt, exclude_first_option=True)
    rgs_cities_id = parser.parse_select_dict(raw_select=rgs_opt, exclude_first_option=True)
    roraima_cities_id = parser.parse_select_dict(raw_select=roraima_opt, exclude_first_option=True)
    sc_cities_id = parser.parse_select_dict(raw_select=sc_opt, exclude_first_option=True)
    sp_cities_id = parser.parse_select_dict(raw_select=sp_opt, exclude_first_option=True)
    sergipe_cities_id = parser.parse_select_dict(raw_select=sergipe_opt, exclude_first_option=True)

    states_city_for_each_state = {
        states_id['amazonas']: amazonas_cities_id,
        states_id['bahia']: bahia_cities_id,
        states_id['distrito_federal']: df_cities_id,
        states_id['goias']: goias_cities_id,
        states_id['maranhao']: maranhao_cities_id,
        states_id['mato_grosso']: mg_cities_id,
        states_id['minas_gerais']: minas_gerais_cities_id,
        states_id['para']: para_cities_id,
        states_id['paraiba']: paraiba_cities_id,
        states_id['parana']: parana_cities_id,
        states_id['pernambuco']: pernambuco_cities_id,
        states_id['piaui']: piaui_cities_id,
        states_id['rio_de_janeiro']: rj_cities_id,
        states_id['rio_grande_do_norte']: rgn_cities_id,
        states_id['rio_grande_do_sul']: rgs_cities_id,
        states_id['roraima']: roraima_cities_id,
        states_id['santa_catarina']: sc_cities_id,
        states_id['sao_paulo']: sp_cities_id,
        states_id['sergipe']: sergipe_cities_id,
    }

    start_urls = ['https://www.leilaovip.com.br/']

    def parse(self, response):

        global estado, cidade
        if self.city in self.states_id:
            estado = self.states_id[self.city]
            cidade = ''
        else:
            for state_id, state_cities in self.states_city_for_each_state.items():
                for city, city_id in state_cities.items():
                    if city == self.city:
                        estado = state_id
                        cidade = city_id

        if self.category == GTEnum.RESIDENTIAL:
            subclasse = '29'
        elif self.category == GTEnum.COMMERCIAL:
            subclasse = '63'
        elif self.category == GTEnum.RURAL:
            subclasse = '33'
        else:
            subclasse = ''

        url = f'https://www.leilaovip.com.br/pesquisa?&estado={estado}&cidade={cidade}&subclasse={subclasse}'

        yield Request(url=url, callback=self.parse_response)

    def parse_response(self, response):
        item = AuctionsItem()

        divs = response.xpath(
            '//div[@class="padding-null auction-card col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"]').extract()
        for div in divs:
            item['site'] = 'Leilão VIP'

            _, dollar_sign, price = self.parser.get_multiple_values_from_string(raw_string=div,
                                                                                xpath='//p[@class="pl-4"][1]').partition(
                'R$')

            price = self.parser.clean_html_tags_from_string(price)

            item['price'] = dollar_sign + ' ' + price

            url = self.parser.get_multiple_values_from_string(raw_string=div, xpath='//a/@href')
            item['url'] = 'https://www.leilaovip.com.br' + url

            yield response.follow(url=url, callback=self.parse_description, cb_kwargs=item)

    def parse_description(self, response, **kwargs):
        item = kwargs

        item['description'] = self.parser.get_multiple_values_from_string(raw_string=response.text, xpath='//span[@id="Holder_lblDescricao"]/text()')

        yield item
