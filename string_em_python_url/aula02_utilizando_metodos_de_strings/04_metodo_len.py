url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

index_interrogacao = url.find('?')
url_base = url[:index_interrogacao]
url_parametros = url[index_interrogacao + 1:]

# buscando especificamente a moeda de origem na url
busca_moeda_origem = 'moedaOrigem'
index_busca_moeda_origem = url_parametros.find(busca_moeda_origem)

index_moeda_origem = index_busca_moeda_origem + len(busca_moeda_origem) + 1

print(url_parametros[index_moeda_origem:])  # só deu certo até o final pq é a última coisa da str

# melhorar na próxima aula
