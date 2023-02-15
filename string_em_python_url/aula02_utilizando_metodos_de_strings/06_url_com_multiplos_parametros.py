url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"

# separa base e os parametros
index_interrogacao = url.find('?')
url_base = url[:index_interrogacao]
url_parametros = url[index_interrogacao + 1:]

# buscando o valor de um parametro
parametro_busca = 'quantidade'
index_parametro = url_parametros.find(parametro_busca)
index_valor = index_parametro + len(parametro_busca) + 1
index_e_comercial = url_parametros.find('&', index_valor) # Esse segundo parâmetro passado ao find(),
                                                          # faz com que o find busque, no caso "&",
                                                          # somente depois desse index passado no segundo parâmetro.
                                                          # Se ele não achar, ele retorna: -1

if index_e_comercial == -1: # se o find não achar '&' ele retorna -1,
                            # o que quer dizer que o valor esta no final da url
                            # entao pode ser impressa do index_valor até o final
    valor = url_parametros[index_valor:]
else:
    valor = url_parametros[index_valor:index_e_comercial]
print(valor)


