from string_em_python_url.extrator_url import ExtratorURL

url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'

extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)

print(f'Iguais? {extrator_url == extrator_url2}')  # este método ainda não funciona, pois o '=='
                                                   # está só comparando o endereço de memória
                                                   # desses 2 objetos.
                                                   # O que falta? O método __eq__ na nossa classe

'''    def __eq__(self, other):
        return self.url == other.url # ou 'other' sem '.url' '''

print(f'\n{extrator_url} -- Memória: {id(extrator_url)}')

print(f'\n{extrator_url2} -- Memória: {id(extrator_url2)}')

# os objetos podem ser IGUAIS, mas não são IDENTICOS

# 'is' vs '=='
# 'is' para Identidade
# '==' para Igualdade
