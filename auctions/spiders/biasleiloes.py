import scrapy
from scrapy import Request

from ..items import AuctionsItem
from ..utils.parser import Parser
from ..constants.constants import GroundTypeEnum as GTEnum

class BiasleiloesSpider(scrapy.Spider):
    name = 'biasleiloes'
    parser = Parser()

    states_opt = """<select id="LoteEstado" class="form-control select-search-estado">
<option uf="AL" class="optUF" value="14">AL (3)</option>
<option uf="AM" class="optUF" value="3">AM (2)</option>
<option uf="BA" class="optUF" value="16">BA (6)</option>
<option uf="CE" class="optUF" value="10">CE (5)</option>
<option uf="GO" class="optUF" value="26">GO (46)</option>
<option uf="MA" class="optUF" value="8">MA (1)</option>
<option uf="MG" class="optUF" value="17">MG (20)</option>
<option uf="MS" class="optUF" value="24">MS (4)</option>
<option uf="MT" class="optUF" value="25">MT (1)</option>
<option uf="PA" class="optUF" value="5">PA (23)</option>
<option uf="PB" class="optUF" value="12">PB (35)</option>
<option uf="PE" class="optUF" value="13">PE (7)</option>
<option uf="PI" class="optUF" value="9">PI (15)</option>
<option uf="PR" class="optUF" value="21">PR (10)</option>
<option uf="RJ" class="optUF" value="19">RJ (27)</option>
<option uf="RN" class="optUF" value="11">RN (2)</option>
<option uf="RO" class="optUF" value="1">RO (1)</option>
<option uf="RS" class="optUF" value="23">RS (8)</option>
<option uf="SC" class="optUF" value="22">SC (4)</option>
<option uf="SE" class="optUF" value="15">SE (6)</option>
<option selected="" uf="SP" class="optUF" value="20">SP (49)</option>
</select>"""
    amazonas_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="114" nome="manacapuru">Manacapuru (1)</option><option value="127" nome="manaus">Manaus (1)</option></select>'
    bahia_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="1776" nome="barreiras">Barreiras (1)</option><option value="3865" nome="camacari">Camaçari (2)</option><option value="3489" nome="iacu">Iaçu (1)</option><option value="3810" nome="salvador">Salvador (1)</option><option value="3301" nome="vitoria-da-conquista">Vitória da Conquista (1)</option></select>'
    ceara_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="3905" nome="aquiraz">Aquiraz (1)</option><option value="3886" nome="fortaleza">Fortaleza (3)</option><option value="3776" nome="penaforte">Penaforte (1)</option></select>'
    goias_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="5769" nome="adelandia">Adelândia (1)</option><option value="1216" nome="aguas-lindas-de-goias">Águas Lindas de Goiás (17)</option><option value="1664" nome="campos-belos">Campos Belos (1)</option><option value="1332" nome="cidade-ocidental">Cidade Ocidental (4)</option><option value="1212" nome="luziania">Luziânia (6)</option><option value="1169" nome="padre-bernardo">Padre Bernardo (3)</option><option value="1297" nome="planaltina">Planaltina (2)</option><option value="1209" nome="santo-antonio-do-descoberto">Santo Antônio do Descoberto (4)</option><option value="1310" nome="valparaiso-de-goias">Valparaíso de Goiás (8)</option></select>'
    maranhao_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="2052" nome="moncao">Monção (1)</option></select>'
    minas_gerais_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="2392" nome="belo-horizonte">Belo Horizonte (1)</option><option value="2289" nome="betim">Betim (3)</option><option value="2356" nome="contagem">Contagem (2)</option><option value="2229" nome="esmeraldas">Esmeraldas (1)</option><option value="1836" nome="formiga">Formiga (1)</option><option value="2367" nome="ibirite">Ibirité (1)</option><option value="2189" nome="itatiaiucu">Itatiaiuçu (1)</option><option value="2207" nome="mateus-leme">Mateus Leme (1)</option><option value="1757" nome="pouso-alegre">Pouso Alegre (1)</option><option value="2251" nome="sete-lagoas">Sete Lagoas (4)</option><option value="2785" nome="timoteo">Timóteo (1)</option><option value="2656" nome="uba">Ubá (1)</option><option value="1201" nome="uberaba">Uberaba (1)</option><option value="2423" nome="vespasiano">Vespasiano (1)</option></select>'
    mg_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="247" nome="cuiaba">Cuiabá (1)</option></select>'
    mgs_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="337" nome="campo-grande">Campo Grande (4)</option></select>'
    parana_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="267" nome="altamira">Altamira (1)</option><option value="1369" nome="aurora-do-para">Aurora do Pará (3)</option><option value="1378" nome="castanhal">Castanhal (1)</option><option value="780" nome="curionopolis">Curionópolis (1)</option><option value="1400" nome="curuca">Curuçá (7)</option><option value="1110" nome="ipixuna-do-para">Ipixuna do Pará (1)</option><option value="1144" nome="paragominas">Paragominas (1)</option><option value="1286" nome="santa-barbara-do-para">Santa Bárbara do Pará (1)</option><option value="1312" nome="santa-isabel-do-para">Santa Isabel do Pará (1)</option><option value="1487" nome="santa-maria-do-para">Santa Maria do Pará (6)</option></select>'
    paraiba_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="4084" nome="belem-do-brejo-do-cruz">Belém do Brejo do Cruz (16)</option><option value="4085" nome="brejo-do-cruz">Brejo do Cruz (6)</option><option value="3855" nome="cajazeiras">Cajazeiras (1)</option><option value="4371" nome="campina-grande">Campina Grande (1)</option><option value="4626" nome="joao-pessoa">João Pessoa (4)</option><option value="4276" nome="juazeirinho">Juazeirinho (1)</option><option value="4054" nome="paulista">Paulista (2)</option><option value="4354" nome="pocinhos">Pocinhos (1)</option><option value="4607" nome="santa-rita">Santa Rita (3)</option></select>'
    pernambuco_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="4619" nome="camaragibe">Camaragibe (1)</option><option value="4037" nome="carnaiba">Carnaíba (1)</option><option value="4547" nome="lagoa-do-carro">Lagoa do Carro (1)</option><option value="4207" nome="pesqueira">Pesqueira (1)</option><option value="4620" nome="recife">Recife (1)</option><option value="3863" nome="serra-talhada">Serra Talhada (1)</option><option value="4431" nome="surubim">Surubim (1)</option></select>'
    piaui_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="3036" nome="altos">Altos (1)</option><option value="3247" nome="parnaiba">Parnaíba (1)</option><option value="3233" nome="piracuruca">Piracuruca (9)</option><option value="2911" nome="sao-pedro-do-piaui">São Pedro do Piauí (4)</option></select>'
    parana_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="5110" nome="colorado">Colorado (1)</option><option value="798" nome="curitiba">Curitiba (1)</option><option value="375" nome="foz-do-iguacu">Foz do Iguaçu (1)</option><option value="5401" nome="londrina">Londrina (1)</option><option value="5102" nome="maringa">Maringá (1)</option><option value="504" nome="perola">Pérola (3)</option><option value="5628" nome="ponta-grossa">Ponta Grossa (1)</option><option value="849" nome="sao-jose-dos-pinhais">São José dos Pinhais (1)</option></select>'
    rj_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="2989" nome="campos-dos-goytacazes">Campos dos Goytacazes (1)</option><option value="2636" nome="itaborai">Itaboraí (1)</option><option value="2856" nome="macae">Macaé (1)</option><option value="2631" nome="marica">Maricá (1)</option><option value="2606" nome="niteroi">Niterói (2)</option><option value="2727" nome="nova-friburgo">Nova Friburgo (1)</option><option value="2461" nome="nova-iguacu">Nova Iguaçu (1)</option><option value="2417" nome="rio-de-janeiro">Rio de Janeiro (13)</option><option value="2613" nome="sao-goncalo">São Gonçalo (6)</option></select>'
    rgn_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="4597" nome="canguaretama">Canguaretama (1)</option><option value="4530" nome="ceara-mirim">Ceará-Mirim (1)</option></select>'
    rgs_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="5598" nome="balneario-pinhal">Balneário Pinhal (1)</option><option value="5368" nome="canoas">Canoas (1)</option><option value="5005" nome="getulio-vargas">Getúlio Vargas (1)</option><option value="5398" nome="novo-hamburgo">Novo Hamburgo (1)</option><option value="5345" nome="porto-alegre">Porto Alegre (2)</option><option value="4879" nome="rio-grande">Rio Grande (2)</option></select>'
    rondonia_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="4597" nome="canguaretama">Canguaretama (1)</option><option value="4530" nome="ceara-mirim">Ceará-Mirim (1)</option></select>'
    roraima_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="104" nome="rolim-de-moura">Rolim de Moura (1)</option></select>'
    sc_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="699" nome="criciuma">Criciúma (1)</option><option value="919" nome="guaramirim">Guaramirim (1)</option><option value="748" nome="icara">Içara (1)</option><option value="1009" nome="sao-jose">São José (1)</option></select>'
    sergipe_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="4145" nome="capela">Capela (2)</option><option value="3925" nome="tobias-barreto">Tobias Barreto (4)</option></select>'
    sp_opt = '<select class="form-control" id="LoteCidade"><option value="0" nome=""> Todas as Cidades </option><option value="5613" nome="assis">Assis (2)</option><option value="1592" nome="braganca-paulista">Bragança Paulista (1)</option><option value="1845" nome="campos-do-jordao">Campos do Jordão (1)</option><option value="1520" nome="itapecerica-da-serra">Itapecerica da Serra (1)</option><option value="1536" nome="itatiba">Itatiba (1)</option><option value="1728" nome="jacarei">Jacareí (1)</option><option value="1079" nome="jau">Jaú (1)</option><option value="1506" nome="jundiai">Jundiaí (1)</option><option value="1600" nome="mairipora">Mairiporã (1)</option><option value="778" nome="mirassol">Mirassol (4)</option><option value="1233" nome="piracicaba">Piracicaba (1)</option><option value="1611" nome="praia-grande">Praia Grande (3)</option><option value="1274" nome="ribeirao-preto">Ribeirão Preto (7)</option><option value="1379" nome="santa-barbara-d\'oeste">Santa Bárbara D\'Oeste (1)</option><option value="1661" nome="santos">Santos (2)</option><option value="1601" nome="sao-bernardo-do-campo">São Bernardo do Campo (1)</option><option value="837" nome="sao-jose-do-rio-preto">São José do Rio Preto (5)</option><option value="1554" nome="sao-paulo">São Paulo (12)</option><option value="1357" nome="sorocaba">Sorocaba (1)</option><option value="5770" nome="votuporanga">Votuporanga (1)</option></select>'

    states_id = {'amazonas': 'am', 'bahia': 'ba', 'ceara': 'ce', 'espirito_santo': 'es', 'goias': 'go', 'maranhao': 'ma', 'mato_grosso': 'mt', 'mato_grosso_do_sul': 'ms', 'minas_gerais': 'mg', 'parana': 'pr', 'paraiba': 'pb', 'para': 'pa', 'pernambuco': 'pe', 'piaui': 'pi', 'rio_grande_do_norte': 'rn', 'rio_grande_do_sul': 'rs', 'rondonia': 'rn','roraima': 'ro','rio_de_janeiro': 'rj', 'santa_catarina': 'sc', 'sergipe': 'se', 'sao_paulo': 'sp', 'tocantins': 'to'}
    amazonas_cities_id = parser.parse_select_dict(raw_select=amazonas_opt,exclude_first_option=True)
    bahia_cities_id = parser.parse_select_dict(raw_select=bahia_opt,exclude_first_option=True)
    ceara_cities_id = parser.parse_select_dict(raw_select=ceara_opt,exclude_first_option=True)
    goias_cities_id = parser.parse_select_dict(raw_select=goias_opt,exclude_first_option=True)
    maranhao_cities_id = parser.parse_select_dict(raw_select=maranhao_opt,exclude_first_option=True)
    mg_cities_id = parser.parse_select_dict(raw_select=mg_opt,exclude_first_option=True)
    mgs_cities_id = parser.parse_select_dict(raw_select=mgs_opt,exclude_first_option=True)
    minas_gerais_cities_id = parser.parse_select_dict(raw_select=minas_gerais_opt,exclude_first_option=True)
    paraiba_cities_id = parser.parse_select_dict(raw_select=paraiba_opt,exclude_first_option=True)
    parana_cities_id = parser.parse_select_dict(raw_select=parana_opt,exclude_first_option=True)
    pernambuco_cities_id = parser.parse_select_dict(raw_select=pernambuco_opt,exclude_first_option=True)
    piaui_cities_id = parser.parse_select_dict(raw_select=piaui_opt,exclude_first_option=True)
    rj_cities_id = parser.parse_select_dict(raw_select=rj_opt,exclude_first_option=True)
    rgn_cities_id = parser.parse_select_dict(raw_select=rgn_opt,exclude_first_option=True)
    rgs_cities_id = parser.parse_select_dict(raw_select=rgs_opt,exclude_first_option=True)
    rondonia_cities_id = parser.parse_select_dict(raw_select=rondonia_opt,exclude_first_option=True)
    roraima_cities_id = parser.parse_select_dict(raw_select=roraima_opt,exclude_first_option=True)
    sc_cities_id = parser.parse_select_dict(raw_select=sc_opt,exclude_first_option=True)
    sp_cities_id = parser.parse_select_dict(raw_select=sp_opt,exclude_first_option=True)
    sergipe_cities_id = parser.parse_select_dict(raw_select=sergipe_opt,exclude_first_option=True)

    states_city_for_each_state = {
        states_id['amazonas']: amazonas_cities_id,
        states_id['bahia']: bahia_cities_id,
        states_id['ceara']: ceara_cities_id,
        states_id['goias']: goias_cities_id,
        states_id['maranhao']: maranhao_cities_id,
        states_id['mato_grosso']: mg_cities_id,
        states_id['mato_grosso_do_sul']: mgs_cities_id,
        states_id['minas_gerais']: minas_gerais_cities_id,
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

    start_urls = ['https://www.biasileiloes.com.br/']

    def parse(self, response):
        global data_bem_estado_id, data_bem_cidade_id, data_bem_categoria_id

        if self.city in self.states_id:
            data_bem_estado_id = self.states_id[self.city]
            data_bem_cidade_id = 'todas-as-cidades'
        else:
            for state_id, state_cities in self.states_city_for_each_state.items():
                for city, city_id in state_cities.items():
                    before, _, _ = city.partition('_(')
                    if before == self.city:
                        data_bem_estado_id = state_id
                        data_bem_cidade_id = before.replace('_','-')

        if self.category == GTEnum.RESIDENTIAL:
            subclasse = 'residenciais'
        elif self.category == GTEnum.COMMERCIAL:
            subclasse = 'comerciais'
        elif self.category == GTEnum.RURAL:
            subclasse = 'terrenos'
        else:
            subclasse = 'todos-os-segmentos'


        token = response.xpath('//input[@name="__RequestVerificationToken"]/@value').get()


        url = f'https://www.biasileiloes.com.br/Sale/LotListSearch?categoria=&subcategoria=&term=&start=0&limit=20&listaId=&slug=&buscaImovel=true&estado={data_bem_estado_id}&bairro=todos-os-bairros&cidade={data_bem_cidade_id}&segmento={subclasse}&__RequestVerificationToken={token}'

        yield Request(url=url, callback=self.parse_response)

    def parse_response(self,response):
        item = AuctionsItem()
        divs = response.xpath('//div[@class="thumbnail thumbnail-vitrine-lot item-bid "]').extract()
        for div in divs:
            item['site'] = 'Bias Leilões'

            item['price'] = self.parser.get_single_value_from_string(raw_string=div,xpath='//span[@class="price-line"]/text()')

            item['url'] = 'https://www.biasileiloes.com.br/' + self.parser.get_single_value_from_string(raw_string=div,xpath='//a/@href')

            item['description'] = self.parser.get_single_value_from_string(raw_string=div,xpath='//div[@class="photo-text"]/span/text()')

            yield item
