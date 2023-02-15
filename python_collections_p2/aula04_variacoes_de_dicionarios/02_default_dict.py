# contando palavras no texto
meu_texto = 'rock in roll like in roll the rock rock'
meu_texto = meu_texto.lower()  # texto em minusculo
aparicoes = {}
for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)  # ate agora vira o valor da palavra
    aparicoes[palavra] = ate_agora + 1  # adiciona 1 no valor da palavra
print(aparicoes)

# default dict
from collections import defaultdict

aparicoes = defaultdict(int)  # aparicoes vai ser um dicionário que por padrão
                              # adiciona valor 0 na chave, caso ainda não tenha valor
for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1
print(aparicoes)
