import scrapy
from ..constants.constants import GroundTypeEnum as GTEnum
from ..items import AuctionsItem
from ..utils.parser import Parser


class MegaleiloesSpider(scrapy.Spider):
    name = 'megaleiloes'
    parser = Parser()

    states_opt = """
<option value="am">Amazonas</option>
<option value="ba">Bahia</option>
<option value="ce">Ceará</option>
<option value="es">Espírito Santo</option>
<option value="go">Goiás</option>
<option value="ma">Maranhão</option>
<option value="mt">Mato Grosso</option>
<option value="ms">Mato Grosso do Sul</option>
<option value="mg">Minas Gerais</option>
<option value="pr">Paraná</option>
<option value="pb">Paraíba</option>
<option value="pa">Pará</option>
<option value="pe">Pernambuco</option>
<option value="pi">Piauí</option>
<option value="rn">Rio Grande do Norte</option>
<option value="rs">Rio Grande do Sul</option>
<option value="rj">Rio de Janeiro</option>
<option value="sc">Santa Catarina</option>
<option value="se">Sergipe</option>
<option value="sp">São Paulo</option>
<option value="to">Tocantins</option>
</select>"""
    amazonas_opt = '<option value="manaus">Manaus</option>'
    bahia_opt = '<option value="barreiras">Barreiras</option><option value="camacari">Camaçari</option><option value="ilheus">Ilhéus</option><option value="salvador">Salvador</option><option value="santa-cruz-cabralia">Santa Cruz Cabrália</option></select>'
    ceara_opt = '<option value="fortaleza">Fortaleza</option><option value="maracanau">Maracanaú</option></select>'
    es_opt = '<option value="sao-mateus">São Mateus</option>'
    goias_opt = '<option value="goiania">Goiânia</option><option value="itumbiara">Itumbiara</option><option value="porangatu">Porangatu</option></select>'
    maranhao_opt = '<option value="fortaleza-dos-nogueiras">Fortaleza dos Nogueiras</option><option value="sao-luis">São Luís</option></select>'
    mg_opt = '<option value="chapada-dos-guimaraes">Chapada dos Guimarães</option><option value="colider">Colíder</option><option value="cuiaba">Cuiabá</option><option value="paranatinga">Paranatinga</option><option value="varzea-grande">Várzea Grande</option></select>'
    msg_opt = '<option value="campo-grande">Campo Grande</option>'
    minas_gerais_opt = '<option value="bambui">Bambuí</option><option value="belo-horizonte">Belo Horizonte</option><option value="betim">Betim</option><option value="boa-esperanca">Boa Esperança</option><option value="cataguases">Cataguases</option><option value="conselheiro-lafaiete">Conselheiro Lafaiete</option><option value="coqueiral">Coqueiral</option><option value="divinopolis">Divinópolis</option><option value="guaxupe">Guaxupé</option><option value="jaboticatubas">Jaboticatubas</option><option value="lagoa-santa">Lagoa Santa</option><option value="mateus-leme">Mateus Leme</option><option value="perdizes">Perdizes</option><option value="piracema">Piracema</option><option value="santana-do-paraiso">Santana do Paraíso</option><option value="sete-lagoas">Sete Lagoas</option></select>'
    parana_opt = '<option value="arapongas">Arapongas</option><option value="cambe">Cambé</option><option value="campo-mourao">Campo Mourão</option><option value="curitiba">Curitiba</option><option value="foz-do-iguacu">Foz do Iguaçu</option><option value="maringa">Maringá</option><option value="perola">Pérola</option><option value="turvo">Turvo</option></select>'
    paraiba_opt = '<option value="patos">Patos</option>'
    para_opt = '<option value="santana-do-araguaia">Santana do Araguaia</option>'
    pernambuco_opt = '<option value="cabo-de-santo-agostinho">Cabo de Santo Agostinho</option><option value="caruaru">Caruaru</option><option value="jaboatao-dos-guararapes">Jaboatão dos Guararapes</option><option value="palmares">Palmares</option><option value="paulista">Paulista</option><option value="petrolina">Petrolina</option><option value="recife">Recife</option></select>'
    piaui_opt = '<option value="lagoa-alegre">Lagoa Alegre</option>'
    rgn_opt = '<option value="espirito-santo">Espírito Santo</option><option value="nisia-floresta">Nísia Floresta</option></select>'
    rgs_opt = '<option value="alvorada">Alvorada</option><option value="canela">Canela</option><option value="caxias-do-sul">Caxias do Sul</option><option value="gravatai">Gravataí</option><option value="porto-alegre">Porto Alegre</option><option value="rio-grande">Rio Grande</option><option value="santana-do-livramento">Santana do Livramento</option><option value="uruguaiana">Uruguaiana</option></select>'
    rj_opt = '<option value="araruama">Araruama</option><option value="duque-de-caxias">Duque de Caxias</option><option value="macae">Macaé</option><option value="mangaratiba">Mangaratiba</option><option value="niteroi">Niterói</option><option value="resende">Resende</option><option value="rio-das-ostras">Rio das Ostras</option><option value="rio-de-janeiro">Rio de Janeiro</option><option value="sao-goncalo">São Gonçalo</option><option value="sao-joao-de-meriti">São João de Meriti</option><option value="volta-redonda">Volta Redonda</option></select>'
    sc_opt = '<option value="criciuma">Criciúma</option><option value="florianopolis">Florianópolis</option><option value="icara">Içara</option><option value="itajai">Itajaí</option><option value="joinville">Joinville</option><option value="navegantes">Navegantes</option><option value="sao-jose">São José</option><option value="taio">Taió</option></select>'
    sergipe_opt = '<option value="aracaju">Aracaju</option><option value="monte-alegre-de-sergipe">Monte Alegre de Sergipe</option></select>'
    sp_opt = '<option value="adamantina">Adamantina</option><option value="aguas-de-santa-barbara">Águas de Santa Bárbara</option><option value="amparo">Amparo</option><option value="apiai">Apiaí</option><option value="aracatuba">Araçatuba</option><option value="aracoiaba-da-serra">Araçoiaba da Serra</option><option value="arandu">Arandu</option><option value="arapiraca">Arapiraca</option><option value="araraquara">Araraquara</option><option value="araras">Araras</option><option value="aruja">Arujá</option><option value="assis">Assis</option><option value="atibaia">Atibaia</option><option value="auriflama">Auriflama</option><option value="avare">Avaré</option><option value="barra-bonita">Barra Bonita</option><option value="barretos">Barretos</option><option value="barueri">Barueri</option><option value="bastos">Bastos</option><option value="bauru">Bauru</option><option value="bebedouro">Bebedouro</option><option value="bertioga">Bertioga</option><option value="birigui">Birigüi</option><option value="boituva">Boituva</option><option value="bom-jesus-dos-perdoes">Bom Jesus dos Perdões</option><option value="botucatu">Botucatu</option><option value="braganca-paulista">Bragança Paulista</option><option value="cacapava">Caçapava</option><option value="caieiras">Caieiras</option><option value="cajamar">Cajamar</option><option value="campinas">Campinas</option><option value="campos-do-jordao">Campos do Jordão</option><option value="cananeia">Cananéia</option><option value="capivari">Capivari</option><option value="carapicuiba">Carapicuíba</option><option value="casa-branca">Casa Branca</option><option value="cotia">Cotia</option><option value="cubatao">Cubatão</option><option value="diadema">Diadema</option><option value="dois-corregos">Dois Córregos</option><option value="embu-das-artes">Embu das Artes</option><option value="espirito-santo-do-pinhal">Espírito Santo do Pinhal</option><option value="fernandopolis">Fernandópolis</option><option value="franca">Franca</option><option value="franco-da-rocha">Franco da Rocha</option><option value="garca">Garça</option><option value="general-salgado">General Salgado</option><option value="guapiara">Guapiara</option><option value="guaratingueta">Guaratinguetá</option><option value="guaruja">Guarujá</option><option value="guarulhos">Guarulhos</option><option value="ibiuna">Ibiúna</option><option value="igarata">Igaratá</option><option value="iguape">Iguape</option><option value="ilha-solteira">Ilha Solteira</option><option value="indaiatuba">Indaiatuba</option><option value="itai">Itaí</option><option value="itapecerica-da-serra">Itapecerica da Serra</option><option value="itapevi">Itapevi</option><option value="itapira">Itapira</option><option value="itapolis">Itápolis</option><option value="itaquaquecetuba">Itaquaquecetuba</option><option value="itatiba">Itatiba</option><option value="itupeva">Itupeva</option><option value="jandira">Jandira</option><option value="jarinu">Jarinu</option><option value="jose-bonifacio">José Bonifácio</option><option value="jundiai">Jundiaí</option><option value="junqueiropolis">Junqueirópolis</option><option value="juquitiba">Juquitiba</option><option value="limeira">Limeira</option><option value="lins">Lins</option><option value="lupercio">Lupércio</option><option value="mairipora">Mairiporã</option><option value="marilia">Marília</option><option value="mirassol">Mirassol</option><option value="mogi-das-cruzes">Mogi das Cruzes</option><option value="mogi-guacu">Mogi Guaçu</option><option value="mogi-mirim">Mogi Mirim</option><option value="mongagua">Mongaguá</option><option value="monte-azul-paulista">Monte Azul Paulista</option><option value="nova-odessa">Nova Odessa</option><option value="orlandia">Orlândia</option><option value="osasco">Osasco</option><option value="ourinhos">Ourinhos</option><option value="pacaembu">Pacaembu</option><option value="palmital">Palmital</option><option value="paranapanema">Paranapanema</option><option value="paulinia">Paulínia</option><option value="pedro-de-toledo">Pedro de Toledo</option><option value="pindamonhangaba">Pindamonhangaba</option><option value="piracicaba">Piracicaba</option><option value="poa">Poá</option><option value="praia-grande">Praia Grande</option><option value="presidente-prudente">Presidente Prudente</option><option value="ribeirao-preto">Ribeirão Preto</option><option value="rio-claro">Rio Claro</option><option value="rio-das-pedras">Rio das Pedras</option><option value="rios-das-pedras">Rios das Pedras</option><option value="salto">Salto</option><option value="santa-branca">Santa Branca</option><option value="santa-isabel">Santa Isabel</option><option value="santana-de-parnaiba">Santana de Parnaíba</option><option value="santo-amaro">Santo Amaro</option><option value="santo-andre">Santo André</option><option value="santo-antonio-de-posse">Santo Antônio de Posse</option><option value="santos">Santos</option><option value="sao-bernardo-do-campo">São Bernardo do Campo</option><option value="sao-caetano-do-sul">São Caetano do Sul</option><option value="sao-jose-do-rio-pardo">São José do Rio Pardo</option><option value="sao-jose-do-rio-preto">São José do Rio Preto</option><option value="sao-jose-dos-campos">São José dos Campos</option><option value="sao-paulo">São Paulo</option><option value="sao-vicente">São Vicente</option><option value="sorocaba">Sorocaba</option><option value="sumare">Sumaré</option><option value="suzano">Suzano</option><option value="taboao-da-serra">Taboão da Serra</option><option value="tanabi">Tanabi</option><option value="taquaritinga">Taquaritinga</option><option value="tatui">Tatuí</option><option value="taubate">Taubaté</option><option value="valinhos">Valinhos</option><option value="vera-cruz">Vera Cruz</option><option value="vinhedo">Vinhedo</option><option value="vista-alegre-do-alto">Vista Alegre do Alto</option><option value="votuporanga">Votuporanga</option></select>'
    tocantins_opt = '<option value="ponte-alta-do-tocantins">Ponte Alta do Tocantins</option>'

    states_id = parser.parse_select_dict(raw_select=states_opt)
    amazonas_cities_id = parser.parse_select_dict(raw_select=amazonas_opt)
    bahia_cities_id = parser.parse_select_dict(raw_select=bahia_opt)
    ceara_cities_id = parser.parse_select_dict(raw_select=ceara_opt)
    es_cities_id = parser.parse_select_dict(raw_select=es_opt)
    goias_cities_id = parser.parse_select_dict(raw_select=goias_opt)
    maranhao_cities_id = parser.parse_select_dict(raw_select=maranhao_opt)
    mg_cities_id = parser.parse_select_dict(raw_select=mg_opt)
    mgs_cities_id = parser.parse_select_dict(raw_select=msg_opt)
    minas_gerais_cities_id = parser.parse_select_dict(raw_select=minas_gerais_opt)
    parana_cities_id = parser.parse_select_dict(raw_select=parana_opt)
    paraiba_cities_id = parser.parse_select_dict(raw_select=paraiba_opt)
    para_cities_id = parser.parse_select_dict(raw_select=para_opt)
    pernambuco_cities_id = parser.parse_select_dict(raw_select=pernambuco_opt)
    piaui_cities_id = parser.parse_select_dict(raw_select=piaui_opt)
    rgn_cities_id = parser.parse_select_dict(raw_select=rgn_opt)
    rgs_cities_id = parser.parse_select_dict(raw_select=rgs_opt)
    rj_cities_id = parser.parse_select_dict(raw_select=rj_opt)
    sc_cities_id = parser.parse_select_dict(raw_select=sc_opt)
    sergipe_cities_id = parser.parse_select_dict(raw_select=sergipe_opt)
    sp_cities_id = parser.parse_select_dict(raw_select=sp_opt)
    tocantins_cities_id = parser.parse_select_dict(raw_select=tocantins_opt)

    # {'acre': '1', 'alagoas': '2', 'amapa': '4', 'amazonas': '3', 'bahia': '5', 'ceara': '6', 'distrito_federal': '7', 'espirito_santo': '8', 'goias': '9', 'maranhao': '10', 'mato_grosso': '13', 'mato_grosso_do_sul': '12', 'minas_gerais': '11', 'para': '14', 'paraiba': '15', 'parana': '18', 'pernambuco': '16', 'piaui': '17', 'rio_de_janeiro': '19', 'rio_grande_do_norte': '20', 'rio_grande_do_sul': '23', 'rondonia': '21', 'roraima': '22', 'santa_catarina': '24', 'sao_paulo': '26', 'sergipe': '25', 'tocantins': '27'}

    states_city_for_each_state = {
        states_id['amazonas']: amazonas_cities_id,
        states_id['bahia']: bahia_cities_id,
        states_id['ceara']: ceara_cities_id,
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

    def __init__(self, city, category):

        base_url = 'https://www.megaleiloes.com.br/imoveis/'
        if category == GTEnum.RESIDENTIAL:
            base_url += 'casas'
        elif category == GTEnum.RURAL:
            base_url += 'imoveis-rurais'
        elif category == GTEnum.COMMERCIAL:
            base_url += 'imoveis-comerciais'

        if city in self.states_id:
            self.start_urls = [f'{base_url}/{self.states_id[city]}']
        else:
            for state_id, state_cities in self.states_city_for_each_state.items():
                for city_key, city_value in state_cities.items():
                    if city_key == city:
                        self.start_urls = [f'{base_url}/{state_id}/{city_value}']

        # self.start_urls = ['http://www.megaleiloes.com.br/']

    def parse(self, response):
        item = AuctionsItem()
        divs = response.xpath('//div[@class="card open"]').extract()

        for div in divs:
            item['site'] = 'Mega Leilões'

            item['price'] = self.parser.get_single_value_from_string(raw_string=div,
                                                                     xpath='//span[@class="card-instance-value"]/text()')

            url = self.parser.get_single_value_from_string(raw_string=div, xpath='//a/@href')
            item['url'] = url

            yield response.follow(url=url, callback=self.parse_description, cb_kwargs=item)

    def parse_description(self, response, **kwargs):
        item = kwargs

        item['description'] = response.xpath('//div[@class="content"]/text()').get().strip()

        yield item
