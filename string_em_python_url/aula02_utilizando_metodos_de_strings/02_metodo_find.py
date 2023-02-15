url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar"

interrogacao_index = url.find('?')


url_base = url[:interrogacao_index]
print(f'Base: {url_base}')

url_parametros = url[interrogacao_index+1:]
print(f'Parâmetros: {url_parametros}')

