import scrapy
from scrapy import Request

from ..utils.parser import Parser
from ..items import AuctionsItem


class ZukermanSpider(scrapy.Spider):
    name = 'zukerman'
    parser = Parser()

    sp_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><optgroup label="&nbsp;"></optgroup><option value="r|1" class="opt-g" ptype="r" pkey="capital">SÃO PAULO - CAPITAL (129)</option><option value="c|São Paulo" class="opt-n" ptype="c" pkey="sao-paulo" prsp="capital">São Paulo (129)</option><optgroup label="&nbsp;"></optgroup><option value="r|4" class="opt-g" ptype="r" pkey="grande-sp">GRANDE SÃO PAULO (67)</option><option value="c|Barueri" class="opt-n" ptype="c" pkey="barueri" prsp="grande-sp">Barueri (18)</option><option value="c|Caieiras" class="opt-n" ptype="c" pkey="caieiras" prsp="grande-sp">Caieiras (1)</option><option value="c|Cotia" class="opt-n" ptype="c" pkey="cotia" prsp="grande-sp">Cotia (4)</option><option value="c|Diadema" class="opt-n" ptype="c" pkey="diadema" prsp="grande-sp">Diadema (3)</option><option value="c|Guarulhos" class="opt-n" ptype="c" pkey="guarulhos" prsp="grande-sp">Guarulhos (1)</option><option value="c|Itaquaquecetuba" class="opt-n" ptype="c" pkey="itaquaquecetuba" prsp="grande-sp">Itaquaquecetuba (1)</option><option value="c|Santana de Parnaíba" class="opt-n" ptype="c" pkey="santana-de-parnaiba" prsp="grande-sp">Santana de Parnaíba (29)</option><option value="c|Santo André" class="opt-n" ptype="c" pkey="santo-andre" prsp="grande-sp">Santo André (2)</option><option value="c|São Bernardo do Campo" class="opt-n" ptype="c" pkey="sao-bernardo-do-campo" prsp="grande-sp">São Bernardo do Campo (8)</option><optgroup label="&nbsp;"></optgroup><option value="r|2" class="opt-g" ptype="r" pkey="interior">INTERIOR DE SÃO PAULO (121)</option><option value="c|Americana" class="opt-n" ptype="c" pkey="americana" prsp="interior">Americana (1)</option><option value="c|Amparo" class="opt-n" ptype="c" pkey="amparo" prsp="interior">Amparo (1)</option><option value="c|Angatuba" class="opt-n" ptype="c" pkey="angatuba" prsp="interior">Angatuba (1)</option><option value="c|Araçoiaba da Serra" class="opt-n" ptype="c" pkey="aracoiaba-da-serra" prsp="interior">Araçoiaba da Serra (2)</option><option value="c|Arandu" class="opt-n" ptype="c" pkey="arandu" prsp="interior">Arandu (1)</option><option value="c|Araraquara" class="opt-n" ptype="c" pkey="araraquara" prsp="interior">Araraquara (1)</option><option value="c|Assis" class="opt-n" ptype="c" pkey="assis" prsp="interior">Assis (3)</option><option value="c|Atibaia" class="opt-n" ptype="c" pkey="atibaia" prsp="interior">Atibaia (2)</option><option value="c|Águas Sta Bárbara" class="opt-n" ptype="c" pkey="aguas-sta-barbara" prsp="interior">Águas Sta Bárbara (1)</option><option value="c|Batatais" class="opt-n" ptype="c" pkey="batatais" prsp="interior">Batatais (1)</option><option value="c|Bauru" class="opt-n" ptype="c" pkey="bauru" prsp="interior">Bauru (7)</option><option value="c|Bocaina" class="opt-n" ptype="c" pkey="bocaina" prsp="interior">Bocaina (1)</option><option value="c|Cabreúva" class="opt-n" ptype="c" pkey="cabreuva" prsp="interior">Cabreúva (1)</option><option value="c|Caçapava" class="opt-n" ptype="c" pkey="cacapava" prsp="interior">Caçapava (2)</option><option value="c|Cajamar" class="opt-n" ptype="c" pkey="cajamar" prsp="interior">Cajamar (1)</option><option value="c|Campinas" class="opt-n" ptype="c" pkey="campinas" prsp="interior">Campinas (4)</option><option value="c|Campo Limpo Paulista" class="opt-n" ptype="c" pkey="campo-limpo-paulista" prsp="interior">Campo Limpo Paulista (1)</option><option value="c|Capela do Alto" class="opt-n" ptype="c" pkey="capela-do-alto" prsp="interior">Capela do Alto (1)</option><option value="c|Dracena" class="opt-n" ptype="c" pkey="dracena" prsp="interior">Dracena (1)</option><option value="c|Guaratinguetá" class="opt-n" ptype="c" pkey="guaratingueta" prsp="interior">Guaratinguetá (1)</option><option value="c|Hortolândia" class="opt-n" ptype="c" pkey="hortolandia" prsp="interior">Hortolândia (2)</option><option value="c|Indaiatuba" class="opt-n" ptype="c" pkey="indaiatuba" prsp="interior">Indaiatuba (3)</option><option value="c|Itapetininga" class="opt-n" ptype="c" pkey="itapetininga" prsp="interior">Itapetininga (1)</option><option value="c|Itapevi" class="opt-n" ptype="c" pkey="itapevi" prsp="interior">Itapevi (3)</option><option value="c|Itatiba" class="opt-n" ptype="c" pkey="itatiba" prsp="interior">Itatiba (5)</option><option value="c|Itu" class="opt-n" ptype="c" pkey="itu" prsp="interior">Itu (4)</option><option value="c|Jaboticabal" class="opt-n" ptype="c" pkey="jaboticabal" prsp="interior">Jaboticabal (2)</option><option value="c|Jacareí" class="opt-n" ptype="c" pkey="jacarei" prsp="interior">Jacareí (1)</option><option value="c|Jardinópolis" class="opt-n" ptype="c" pkey="jardinopolis" prsp="interior">Jardinópolis (1)</option><option value="c|Jaú" class="opt-n" ptype="c" pkey="jau" prsp="interior">Jaú (2)</option><option value="c|Jundiaí" class="opt-n" ptype="c" pkey="jundiai" prsp="interior">Jundiaí (1)</option><option value="c|Limeira" class="opt-n" ptype="c" pkey="limeira" prsp="interior">Limeira (3)</option><option value="c|Luís Antônio" class="opt-n" ptype="c" pkey="luis-antonio" prsp="interior">Luís Antônio (1)</option><option value="c|Marília" class="opt-n" ptype="c" pkey="marilia" prsp="interior">Marília (2)</option><option value="c|Mogi das Cruzes" class="opt-n" ptype="c" pkey="mogi-das-cruzes" prsp="interior">Mogi das Cruzes (3)</option><option value="c|Mogi Mirim" class="opt-n" ptype="c" pkey="mogi-mirim" prsp="interior">Mogi Mirim (1)</option><option value="c|Nova Odessa" class="opt-n" ptype="c" pkey="nova-odessa" prsp="interior">Nova Odessa (1)</option><option value="c|Novais" class="opt-n" ptype="c" pkey="novais" prsp="interior">Novais (6)</option><option value="c|Orlândia" class="opt-n" ptype="c" pkey="orlandia" prsp="interior">Orlândia (1)</option><option value="c|Paulínia" class="opt-n" ptype="c" pkey="paulinia" prsp="interior">Paulínia (1)</option><option value="c|Piedade" class="opt-n" ptype="c" pkey="piedade" prsp="interior">Piedade (1)</option><option value="c|Piracicaba" class="opt-n" ptype="c" pkey="piracicaba" prsp="interior">Piracicaba (4)</option><option value="c|Pirapozinho" class="opt-n" ptype="c" pkey="pirapozinho" prsp="interior">Pirapozinho (1)</option><option value="c|Planalto" class="opt-n" ptype="c" pkey="planalto" prsp="interior">Planalto (1)</option><option value="c|Ribeirão Preto" class="opt-n" ptype="c" pkey="ribeirao-preto" prsp="interior">Ribeirão Preto (6)</option><option value="c|Santa Bárbara Doeste" class="opt-n" ptype="c" pkey="santa-barbara-doeste" prsp="interior">Santa Bárbara Doeste (1)</option><option value="c|Santa Isabel" class="opt-n" ptype="c" pkey="santa-isabel" prsp="interior">Santa Isabel (2)</option><option value="c|Santo Antônio de Posse" class="opt-n" ptype="c" pkey="santo-antonio-de-posse" prsp="interior">Santo Antônio de Posse (3)</option><option value="c|São Carlos" class="opt-n" ptype="c" pkey="sao-carlos" prsp="interior">São Carlos (1)</option><option value="c|São José do Rio Preto" class="opt-n" ptype="c" pkey="sao-jose-do-rio-preto" prsp="interior">São José do Rio Preto (1)</option><option value="c|São José dos Campos" class="opt-n" ptype="c" pkey="sao-jose-dos-campos" prsp="interior">São José dos Campos (2)</option><option value="c|São Roque" class="opt-n" ptype="c" pkey="sao-roque" prsp="interior">São Roque (1)</option><option value="c|Sorocaba" class="opt-n" ptype="c" pkey="sorocaba" prsp="interior">Sorocaba (12)</option><option value="c|Sumaré" class="opt-n" ptype="c" pkey="sumare" prsp="interior">Sumaré (1)</option><option value="c|Suzano" class="opt-n" ptype="c" pkey="suzano" prsp="interior">Suzano (1)</option><option value="c|Tarumã" class="opt-n" ptype="c" pkey="taruma" prsp="interior">Tarumã (1)</option><option value="c|Taubaté" class="opt-n" ptype="c" pkey="taubate" prsp="interior">Taubaté (1)</option><option value="c|Vinhedo" class="opt-n" ptype="c" pkey="vinhedo" prsp="interior">Vinhedo (1)</option><option value="c|Votorantim" class="opt-n" ptype="c" pkey="votorantim" prsp="interior">Votorantim (1)</option><option value="c|Votuporanga" class="opt-n" ptype="c" pkey="votuporanga" prsp="interior">Votuporanga (1)</option><optgroup label="&nbsp;"></optgroup><option value="r|3" class="opt-g" ptype="r" pkey="litoral">LITORAL DE SÃO PAULO (25)</option><option value="c|Guarujá" class="opt-n" ptype="c" pkey="guaruja" prsp="litoral">Guarujá (2)</option><option value="c|Ilha Comprida" class="opt-n" ptype="c" pkey="ilha-comprida" prsp="litoral">Ilha Comprida (1)</option><option value="c|Ilhabela" class="opt-n" ptype="c" pkey="ilhabela" prsp="litoral">Ilhabela (1)</option><option value="c|Itanhaém" class="opt-n" ptype="c" pkey="itanhaem" prsp="litoral">Itanhaém (3)</option><option value="c|Mongaguá" class="opt-n" ptype="c" pkey="mongagua" prsp="litoral">Mongaguá (2)</option><option value="c|Praia Grande" class="opt-n" ptype="c" pkey="praia-grande" prsp="litoral">Praia Grande (8)</option><option value="c|Santos" class="opt-n" ptype="c" pkey="santos" prsp="litoral">Santos (5)</option><option value="c|São Sebastião" class="opt-n" ptype="c" pkey="sao-sebastiao" prsp="litoral">São Sebastião (1)</option><option value="c|São Vicente" class="opt-n" ptype="c" pkey="sao-vicente" prsp="litoral">São Vicente (2)</option></select>'
    bahia_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Correntina" class="opt-n" ptype="c" pkey="correntina" prsp="">Correntina (1)</option><option value="c|Guanambi" class="opt-n" ptype="c" pkey="guanambi" prsp="">Guanambi (1)</option><option value="c|Lapão" class="opt-n" ptype="c" pkey="lapao" prsp="">Lapão (1)</option><option value="c|Planaltino" class="opt-n" ptype="c" pkey="planaltino" prsp="">Planaltino (1)</option><option value="c|Salvador" class="opt-n" ptype="c" pkey="salvador" prsp="">Salvador (2)</option><option value="c|Santa Cruz Cabrália" class="opt-n" ptype="c" pkey="santa-cruz-cabralia" prsp="">Santa Cruz Cabrália (3)</option></select>'
    ceara_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Aquiraz" class="opt-n" ptype="c" pkey="aquiraz" prsp="">Aquiraz (1)</option><option value="c|Crateus" class="opt-n" ptype="c" pkey="crateus" prsp="">Crateus (1)</option><option value="c|Fortaleza" class="opt-n" ptype="c" pkey="fortaleza" prsp="">Fortaleza (5)</option><option value="c|Pedra Branca" class="opt-n" ptype="c" pkey="pedra-branca" prsp="">Pedra Branca (1)</option></select>'
    es_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Serra" class="opt-n" ptype="c" pkey="serra" prsp="">Serra (1)</option></select>'
    goias_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Aparecida de Goiânia" class="opt-n" ptype="c" pkey="aparecida-de-goiania" prsp="">Aparecida de Goiânia (1)</option><option value="c|Águas Lindas de Goiás" class="opt-n" ptype="c" pkey="aguas-lindas-de-goias" prsp="">Águas Lindas de Goiás (1)</option><option value="c|Goiânia" class="opt-n" ptype="c" pkey="goiania" prsp="">Goiânia (2)</option><option value="c|Niquelândia" class="opt-n" ptype="c" pkey="niquelandia" prsp="">Niquelândia (1)</option><option value="c|Novo Goiás" class="opt-n" ptype="c" pkey="novo-goias" prsp="">Novo Goiás (1)</option><option value="c|Porangatu" class="opt-n" ptype="c" pkey="porangatu" prsp="">Porangatu (1)</option><option value="c|Valparaíso de Goiás" class="opt-n" ptype="c" pkey="valparaiso-de-goias" prsp="">Valparaíso de Goiás (1)</option></select>'
    maranhao_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Açailândia" class="opt-n" ptype="c" pkey="acailandia" prsp="">Açailândia (1)</option><option value="c|Barra do Corda" class="opt-n" ptype="c" pkey="barra-do-corda" prsp="">Barra do Corda (1)</option></select>'
    minas_gerais_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Belo Horizonte" class="opt-n" ptype="c" pkey="belo-horizonte" prsp="">Belo Horizonte (3)</option><option value="c|Betim" class="opt-n" ptype="c" pkey="betim" prsp="">Betim (3)</option><option value="c|Boa Esperança" class="opt-n" ptype="c" pkey="boa-esperanca" prsp="">Boa Esperança (1)</option><option value="c|Conselheiro Lafaiete" class="opt-n" ptype="c" pkey="conselheiro-lafaiete" prsp="">Conselheiro Lafaiete (1)</option><option value="c|Contagem" class="opt-n" ptype="c" pkey="contagem" prsp="">Contagem (3)</option><option value="c|Divinópolis" class="opt-n" ptype="c" pkey="divinopolis" prsp="">Divinópolis (1)</option><option value="c|Governador Valadares" class="opt-n" ptype="c" pkey="governador-valadares" prsp="">Governador Valadares (1)</option><option value="c|Inhaúma" class="opt-n" ptype="c" pkey="inhauma" prsp="">Inhaúma (2)</option><option value="c|Jaboticatubas" class="opt-n" ptype="c" pkey="jaboticatubas" prsp="">Jaboticatubas (1)</option><option value="c|Jacinto" class="opt-n" ptype="c" pkey="jacinto" prsp="">Jacinto (1)</option><option value="c|Mateus Leme" class="opt-n" ptype="c" pkey="mateus-leme" prsp="">Mateus Leme (1)</option><option value="c|Nova Lima" class="opt-n" ptype="c" pkey="nova-lima" prsp="">Nova Lima (1)</option><option value="c|Santa Vitória" class="opt-n" ptype="c" pkey="santa-vitoria" prsp="">Santa Vitória (1)</option><option value="c|São João Del-Rei" class="opt-n" ptype="c" pkey="sao-joao-del_rei" prsp="">São João Del-Rei (1)</option><option value="c|Sete Lagoas" class="opt-n" ptype="c" pkey="sete-lagoas" prsp="">Sete Lagoas (2)</option><option value="c|Três Corações" class="opt-n" ptype="c" pkey="tres-coracoes" prsp="">Três Corações (1)</option><option value="c|Uberlândia" class="opt-n" ptype="c" pkey="uberlandia" prsp="">Uberlândia (5)</option><option value="c|Viçosa" class="opt-n" ptype="c" pkey="vicosa" prsp="">Viçosa (1)</option></select>'
    mg_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Apiacás" class="opt-n" ptype="c" pkey="apiacas" prsp="">Apiacás (1)</option><option value="c|Colniza" class="opt-n" ptype="c" pkey="colniza" prsp="">Colniza (1)</option><option value="c|Cuiabá" class="opt-n" ptype="c" pkey="cuiaba" prsp="">Cuiabá (2)</option><option value="c|Várzea Grande" class="opt-n" ptype="c" pkey="varzea-grande" prsp="">Várzea Grande (4)</option></select>'
    para_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Altamira" class="opt-n" ptype="c" pkey="altamira" prsp="">Altamira (1)</option><option value="c|Ananindeua" class="opt-n" ptype="c" pkey="ananindeua" prsp="">Ananindeua (1)</option></select>'
    paraiba_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|João Pessoa" class="opt-n" ptype="c" pkey="joao-pessoa" prsp="">João Pessoa (3)</option><option value="c|Mamanguape" class="opt-n" ptype="c" pkey="mamanguape" prsp="">Mamanguape (1)</option></select>'
    pernambuco_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Carpina" class="opt-n" ptype="c" pkey="carpina" prsp="">Carpina (1)</option><option value="c|Gravatá" class="opt-n" ptype="c" pkey="gravata" prsp="">Gravatá (1)</option><option value="c|Ingazeira" class="opt-n" ptype="c" pkey="ingazeira" prsp="">Ingazeira (1)</option><option value="c|Jaboatão dos Guararapes" class="opt-n" ptype="c" pkey="jaboatao-dos-guararapes" prsp="">Jaboatão dos Guararapes (2)</option><option value="c|Moreno" class="opt-n" ptype="c" pkey="moreno" prsp="">Moreno (1)</option><option value="c|Pombos" class="opt-n" ptype="c" pkey="pombos" prsp="">Pombos (1)</option><option value="c|Recife" class="opt-n" ptype="c" pkey="recife" prsp="">Recife (3)</option><option value="c|Santa Cruz do Capibaribe" class="opt-n" ptype="c" pkey="santa-cruz-do-capibaribe" prsp="">Santa Cruz do Capibaribe (1)</option><option value="c|Santa Maria da Boa Vista" class="opt-n" ptype="c" pkey="santa-maria-da-boa-vista" prsp="">Santa Maria da Boa Vista (1)</option><option value="c|Vitória de Santo Antão" class="opt-n" ptype="c" pkey="vitoria-de-santo-antao" prsp="">Vitória de Santo Antão (1)</option></select>'
    parana_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Cascavel" class="opt-n" ptype="c" pkey="cascavel" prsp="">Cascavel (1)</option><option value="c|Curitiba" class="opt-n" ptype="c" pkey="curitiba" prsp="">Curitiba (2)</option><option value="c|Itambé" class="opt-n" ptype="c" pkey="itambe" prsp="">Itambé (1)</option><option value="c|Maringá" class="opt-n" ptype="c" pkey="maringa" prsp="">Maringá (2)</option><option value="c|Pérola" class="opt-n" ptype="c" pkey="perola" prsp="">Pérola (2)</option><option value="c|Ponta Grossa" class="opt-n" ptype="c" pkey="ponta-grossa" prsp="">Ponta Grossa (1)</option><option value="c|Sarandi" class="opt-n" ptype="c" pkey="sarandi" prsp="">Sarandi (1)</option><option value="c|Sertanópolis" class="opt-n" ptype="c" pkey="sertanopolis" prsp="">Sertanópolis (1)</option></select>'
    rj_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Campos dos Goytacazes" class="opt-n" ptype="c" pkey="campos-dos-goytacazes" prsp="">Campos dos Goytacazes (1)</option><option value="c|Iguaba Grande" class="opt-n" ptype="c" pkey="iguaba-grande" prsp="">Iguaba Grande (1)</option><option value="c|Itaboraí" class="opt-n" ptype="c" pkey="itaborai" prsp="">Itaboraí (1)</option><option value="c|Itaguaí" class="opt-n" ptype="c" pkey="itaguai" prsp="">Itaguaí (1)</option><option value="c|Macaé" class="opt-n" ptype="c" pkey="macae" prsp="">Macaé (2)</option><option value="c|Magé" class="opt-n" ptype="c" pkey="mage" prsp="">Magé (1)</option><option value="c|Maricá" class="opt-n" ptype="c" pkey="marica" prsp="">Maricá (1)</option><option value="c|Niterói" class="opt-n" ptype="c" pkey="niteroi" prsp="">Niterói (3)</option><option value="c|Parati" class="opt-n" ptype="c" pkey="parati" prsp="">Parati (1)</option><option value="c|Rio Bonito" class="opt-n" ptype="c" pkey="rio-bonito" prsp="">Rio Bonito (1)</option><option value="c|Rio de Janeiro" class="opt-n" ptype="c" pkey="rio-de-janeiro" prsp="">Rio de Janeiro (39)</option><option value="c|São Gonçalo" class="opt-n" ptype="c" pkey="sao-goncalo" prsp="">São Gonçalo (19)</option><option value="c|São João de Meriti" class="opt-n" ptype="c" pkey="sao-joao-de-meriti" prsp="">São João de Meriti (1)</option><option value="c|Volta Redonda" class="opt-n" ptype="c" pkey="volta-redonda" prsp="">Volta Redonda (1)</option></select>'
    rgn_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Espírito Santo" class="opt-n" ptype="c" pkey="espirito-santo" prsp="">Espírito Santo (1)</option><option value="c|Natal" class="opt-n" ptype="c" pkey="natal" prsp="">Natal (2)</option><option value="c|Nísia Floresta" class="opt-n" ptype="c" pkey="nisia-floresta" prsp="">Nísia Floresta (1)</option></select>'
    rgs_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Cachoeirinha" class="opt-n" ptype="c" pkey="cachoeirinha" prsp="">Cachoeirinha (2)</option><option value="c|Canoas" class="opt-n" ptype="c" pkey="canoas" prsp="">Canoas (1)</option><option value="c|Carazinho" class="opt-n" ptype="c" pkey="carazinho" prsp="">Carazinho (1)</option><option value="c|Cidreira" class="opt-n" ptype="c" pkey="cidreira" prsp="">Cidreira (1)</option><option value="c|Gravataí" class="opt-n" ptype="c" pkey="gravatai" prsp="">Gravataí (3)</option><option value="c|Lajeado" class="opt-n" ptype="c" pkey="lajeado" prsp="">Lajeado (1)</option><option value="c|Passo Fundo" class="opt-n" ptype="c" pkey="passo-fundo" prsp="">Passo Fundo (1)</option><option value="c|Pelotas" class="opt-n" ptype="c" pkey="pelotas" prsp="">Pelotas (1)</option><option value="c|Porto Alegre" class="opt-n" ptype="c" pkey="porto-alegre" prsp="">Porto Alegre (5)</option><option value="c|Rio Grande" class="opt-n" ptype="c" pkey="rio-grande" prsp="">Rio Grande (2)</option><option value="c|Teutônia" class="opt-n" ptype="c" pkey="teutonia" prsp="">Teutônia (1)</option><option value="c|Tramandaí" class="opt-n" ptype="c" pkey="tramandai" prsp="">Tramandaí (1)</option><option value="c|Viamão" class="opt-n" ptype="c" pkey="viamao" prsp="">Viamão (2)</option></select>'
    sc_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Alfredo Wagner" class="opt-n" ptype="c" pkey="alfredo-wagner" prsp="">Alfredo Wagner (1)</option><option value="c|Florianópolis" class="opt-n" ptype="c" pkey="florianopolis" prsp="">Florianópolis (2)</option><option value="c|Schroeder" class="opt-n" ptype="c" pkey="schroeder" prsp="">Schroeder (1)</option></select>'
    sergipe_opt = '<select id="fd-city" name="fd-city" class="fd-city s-fd-select"><option value="c|" class="opt-n" ptype="c" pkey="undefined" prsp="">Todas as cidades</option><option value="c|Aracaju" class="opt-n" ptype="c" pkey="aracaju" prsp="">Aracaju (2)</option><option value="c|Nossa Senhora do Socorro" class="opt-n" ptype="c" pkey="nossa-senhora-do-socorro" prsp="">Nossa Senhora do Socorro (1)</option><option value="c|São Cristóvão" class="opt-n" ptype="c" pkey="sao-cristovao" prsp="">São Cristóvão (1)</option></select>'

    states_id = {'amazonas': 'am', 'bahia': 'ba', 'ceara': 'ce', 'espirito_santo': 'es', 'goias': 'go',
                 'maranhao': 'ma', 'mato_grosso': 'mt', 'mato_grosso_do_sul': 'ms', 'minas_gerais': 'mg',
                 'parana': 'pr', 'paraiba': 'pb', 'para': 'pa', 'pernambuco': 'pe', 'piaui': 'pi',
                 'rio_grande_do_norte': 'rn', 'rio_grande_do_sul': 'rs', 'rondonia': 'rn', 'roraima': 'ro',
                 'rio_de_janeiro': 'rj', 'santa_catarina': 'sc', 'sergipe': 'se', 'sao_paulo': 'sp', 'tocantins': 'to'}
    sp_cities_id = parser._parse_select_dict(raw_select=sp_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    bahia_cities_id = parser._parse_select_dict(raw_select=bahia_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    ceara_cities_id = parser._parse_select_dict(raw_select=ceara_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    es_cities_id = parser._parse_select_dict(raw_select=es_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    goias_cities_id = parser._parse_select_dict(raw_select=goias_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    maranhao_cities_id = parser._parse_select_dict(raw_select=maranhao_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    minas_gerais_cities_id = parser._parse_select_dict(raw_select=minas_gerais_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    mg_cities_id = parser._parse_select_dict(raw_select=mg_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    para_cities_id = parser._parse_select_dict(raw_select=para_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    paraiba_cities_id = parser._parse_select_dict(raw_select=paraiba_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    pernambuco_cities_id = parser._parse_select_dict(raw_select=pernambuco_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    parana_cities_id = parser._parse_select_dict(raw_select=parana_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    rj_cities_id = parser._parse_select_dict(raw_select=rj_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    rgn_cities_id = parser._parse_select_dict(raw_select=rgn_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    rgs_cities_id = parser._parse_select_dict(raw_select=rgs_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    sc_cities_id = parser._parse_select_dict(raw_select=sc_opt, exclude_first_option=True, split_value='pkey', split_key=' (')
    sergipe_cities_id = parser._parse_select_dict(raw_select=sergipe_opt, exclude_first_option=True, split_value='pkey', split_key=' (')

    states_city_for_each_state = {
        states_id['bahia']: bahia_cities_id,
        states_id['ceara']: ceara_cities_id,
        states_id['goias']: goias_cities_id,
        states_id['maranhao']: maranhao_cities_id,
        states_id['mato_grosso']: mg_cities_id,
        states_id['minas_gerais']: minas_gerais_cities_id,
        states_id['paraiba']: paraiba_cities_id,
        states_id['parana']: parana_cities_id,
        states_id['pernambuco']: pernambuco_cities_id,
        states_id['rio_de_janeiro']: rj_cities_id,
        states_id['rio_grande_do_norte']: rgn_cities_id,
        states_id['rio_grande_do_sul']: rgs_cities_id,
        states_id['santa_catarina']: sc_cities_id,
        states_id['sao_paulo']: sp_cities_id,
        states_id['sergipe']: sergipe_cities_id,
    }



    start_urls = ['http://www.zukerman.com.br/']

    def parse(self, response):
        global data_bem_estado_id, data_bem_cidade_id, data_bem_categoria_id

        if self.city in self.states_id:
            estado = self.states_id[self.city]
            cidade = ''
        else:
            for state_id, state_cities in self.states_city_for_each_state.items():
                for city, city_id in state_cities.items():
                    if city == self.city:
                        estado = state_id
                        cidade = city_id

        url = f'https://www.zukerman.com.br/leilao-de-imoveis/{estado}/{cidade}'

        yield Request(url=url, callback=self.parse_response)

    def parse_response(self,response):
        item = AuctionsItem()

        divs = response.xpath('//div[@class="cd-0"]').extract()
        for div in divs:
            item['site'] = 'Zukerman'

            item['price'] = self.parser.get_single_value_from_string(raw_string=div, xpath='//li[@class="cd-it-r4-v1"]/text()').strip()

            url = self.parser.get_single_value_from_string(raw_string=div,xpath='//a/@href')
            item['url'] = url

            yield response.follow(url=url, callback=self.parse_description, cb_kwargs=item)

    def parse_description(self, response, **kwargs):
        item = kwargs

        description = description = response.xpath('//div[@class="s-d-ld-i1 f-d"]//p/text()').extract()
        description = ' '.join(description).strip()


        item['description'] = description

        item['category'] = self.parser.parse_category_based_on_description(description)

        yield item

