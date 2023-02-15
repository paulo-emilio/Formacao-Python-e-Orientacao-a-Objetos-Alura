from collections import Counter

texto1 = '''Python é uma linguagem de programação de alto nível e de uso geral. Sua filosofia de design enfatiza a legibilidade do código com o uso de recuo signthon é tipado dinamicamente e coletado como lixo . Ele oferece suporte a vários paradigmas de programação , incluindo programação estruturada (particularmente processual ), orientada a objetos e funcional . Muitas vezes é brangente.
Guido van Rossum começou a trabalhar em Python no final dos anos 1980 como um sucessor da linguagem de programação ABC e a lançou pela primeira vez em 1991 como Python 0.9.0. O Python 2.0 foi lançado em 2000 e introduziu novos recursos, como compreensão de lista , 
coleta de lixo com detecção de ciclo , contagem de referência e suporte a Unicode . Python 3.0, lançado em 2008, foi uma grande revisão não totalmente compatível com versões anteriores. O Python 2.7.18, lançado em 2020, foi o último lançamento do Python 2. O Python é consistentemente classificado como uma das linguagens de programação mais populares.'''

texto2 = '''Red Dead Redemption 2 é um jogo eletrônico de ação-aventura desenvolvido e publicado pela Rockstar Games. É o terceiro título da série Red Dead e uma prequela de Red Dead Redemption, tendo sido lançado em outubro de 2018 para PlayStation 4 e Xbox One e em novembro de 2019 para Microsoft Windows e Google Stadia. A história se passa em 1899 em uma representação ficcional do oeste, meio-oeste e sul dos Estados Unidos e acompanha o fora da lei Arthur Morgan, que precisa lidar com o declínio do Velho Oeste e sobreviver à perseguição de forças governamentais, gangues rivais e outros adversários.
A jogabilidade é apresentada tanto em uma perspectiva em primeira quanto em terceira pessoa, com o jogador sendo livre para explorar e interagir com o mundo aberto. Elementos de jogabilidade incluem tiroteios, assaltos, caça, cavalgadas, interação com personagens não jogáveis e gerenciamento da honra do protagonista por meio de escolhas morais e atos. Um sistema de recompensa similar àquele presente na série Grand Theft Auto governa as respostas da polícia e caçadores de recompensa aos crimes cometidos pelo jogador. Um modo multijogador chamado de Red Dead Online estreou em novembro de 2018.
O desenvolvimento do título começou logo depois do lançamento de Red Dead Redemption em 2010 e foi compartilhado entre todas desenvolvedoras da Rockstar Games ao redor do mundo. A equipe se inspirou em locais reais, focando-se na criação de uma reflexão fiel do período temporal por meio dos personagens e do mundo de jogo. Red Dead Redemption 2 foi o primeiro jogo da Rockstar Games desenvolvido especificamente para os consoles da oitava geração. A trilha sonora original inclui músicas orquestrais compostas por Woody Jackson e várias faixas vocais produzidas por Daniel Lanois.
Red Dead Redemption 2 foi amplamente antecipado pré-estreia, tendo batido vários recordes e tornado-se o segundo maior lançamento da indústria do entretenimento. Ele arrecadou mais de 725 milhões de dólares em seu fim de semana de estreia e superou as vendas totais do primeiro Red Dead Redemption em apenas duas semanas, já tendo vendido mundialmente mais de 44 milhões de cópias.[1] Ele foi aclamado pela crítica especializada, com elogios direcionados para sua história, personagens, mundo aberto e nível de detalhes. Considerado por múltiplas publicações como um dos melhores jogos eletrônicos de todos os tempos, Red Dead Redemption 2 também venceu diversos prêmios de final de ano, incluindo alguns de Jogo do Ano.'''

aparicoes_caracteres_t1 = Counter(texto1.lower())
print(aparicoes_caracteres_t1)
total_caracteres = sum(aparicoes_caracteres_t1.values())
print(f'\nTotal de Caracteres: {total_caracteres}')

print('\nPorcentagem de cada Caractere:')
for letra, valor in aparicoes_caracteres_t1.items():
    porcentagem = (valor / total_caracteres) * 100
    print(f'|{letra}| - {porcentagem:.2f}%')

# criando um dicionário dessas porcentagens
lista_porcentagem_t1 = [(letra, valor / total_caracteres * 100) for letra, valor in aparicoes_caracteres_t1.items()]
dict_porcentagem_t1 = Counter(dict(lista_porcentagem_t1))
print(dict_porcentagem_t1.most_common(10))





