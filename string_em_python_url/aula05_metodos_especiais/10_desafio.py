from string_em_python_url.extrator_url import ExtratorURL
url = 'bytebank.com/cambio?quantidade=500&moedaOrigem=dolar&moedaDestino=real'
extrator_url = ExtratorURL(url)

valor_dolar = 5
moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
quantidade = int(extrator_url.get_valor_parametro('quantidade'))
moeda_convertida = int

if moeda_origem == 'real' and moeda_destino == 'dolar':
    moeda_convertida = valor_dolar * quantidade
elif moeda_origem == 'dolar' and moeda_destino == 'real':
    moeda_convertida = quantidade / valor_dolar
else:
    print('ERRO: Conversão não disponível!')
print(moeda_convertida)