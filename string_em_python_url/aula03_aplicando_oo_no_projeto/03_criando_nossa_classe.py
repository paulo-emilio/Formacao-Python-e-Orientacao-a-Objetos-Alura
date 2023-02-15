# Criei a classe no pacote 'extrator.url'

from string_em_python_url.extrator_url import *

extrator_url = ExtratorURL('bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100')
# extrator_url = ExtratorURL('   ')
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)