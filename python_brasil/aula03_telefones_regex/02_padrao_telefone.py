from python_brasil.telefonesbr import TelefonesBr
'''
import re

padrao_telefone = '[0-9]{2}[0-9]{4,5}[0-9]{4}'
esse_tel = 'Este é um número de telefone: 31996663269; também tenho esse 3788876633'
resposta = re.findall(padrao_telefone, esse_tel)  # findall acha todas ocorrencias desse padrão
print(resposta)
'''
tel = TelefonesBr('5532987696669')
print(tel)