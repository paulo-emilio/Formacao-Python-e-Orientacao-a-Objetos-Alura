import re
tel = 'esse tel: 5537912345678 vai ser achado'
padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
resposta = re.search(padrao, tel)
# print(resposta.group())
# print(resposta.group(1))  # printa o primeiro grupo (None), pois não tem o código de país e é opcional
# print(resposta.group(3))  # printa o terceiro grupo

from python_brasil.telefonesbr import TelefonesBr

txt = TelefonesBr(tel)
print(txt)

# OBS: O código do professor não funcionava com um dígito a mais (qnd telefone com 9 dígitos):
# Pesquisei e descobri que ex: ([0-9]{2,3}?) esse '?' logo depois da quantidade mostra que deve-se pegar a menor
    # quantidade encontrada, no  cado de +55 37... da certo de pegar só o 55, e nao 557 como antes
# Também descobri o '$' na ultima expressao, fazendo com que seja forçado os 4 ultimos digitos, com isso temos
    # os outros 4 digitos da frente, forçando saber se existe um 9° dígito, ai encainxando o DDD e depois descobrindo
    # se restaram 2 ou 3 dígitos q são o de país
    # NÃO FUNCIONOU
