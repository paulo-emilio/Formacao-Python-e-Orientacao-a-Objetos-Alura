from string_em_python_url.extrator_url import ExtratorURL

url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'

extrator_url = ExtratorURL(url)

# def __len__(self):
#     return len(self.url)

print(f'O tamanho da URL é: {len(extrator_url)}')

# def __str__(self):
#     return self.url

print(f'Sua URL: {extrator_url}')