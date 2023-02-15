'''import re

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
    # usando (https://) diz que o padrão deve ser exatamente aquele, usando [a-z] diz que deve 1 dentre esses caracteres

url = 'bytebank.com.br/cambio'
match = padrao_url.match(url)  # método match descobre se é o padrão é exatamente esse
if not match:
    raise ValueError('URL não é válida')
else:
    print('URL válida')'''

# PASSEI TUDO PARA 'extrator_url'
from string_em_python_url.extrator_url import ExtratorURL

url = 'bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100'
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)
