# url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
url = ' \t'

# SANITIZAÇÃO DA URL
'''url = url.replace(' ', '') # substitui espaços por nada'''
url = url.strip() #substitui além dos espaços antes e depois da str, os caracteres especiais, como: \t

# VALIDAÇÃO DA URL
# raise vai retornar um levantamento de erro, mostando o porquê ocorreu o erro. (url vazia)
if url == '':
    raise ValueError('A URL está vazia')

index_interrogacao = url.find('?')
url_base = url[:index_interrogacao]
url_parametros = url[index_interrogacao + 1:]

parametro_busca = 'quantidade'
index_parametro = url_parametros.find(parametro_busca)
index_valor = index_parametro + len(parametro_busca) + 1
index_e_comercial = url_parametros.find('&', index_valor)

if index_e_comercial == -1:
    valor = url_parametros[index_valor:]
else:
    valor = url_parametros[index_valor:index_e_comercial]
print(valor)


