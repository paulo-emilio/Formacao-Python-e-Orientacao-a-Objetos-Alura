'''# melhorando o Sanitiza e o Valida:

def sanitiza_url(self, url):
    if type(url) == str:     # se o tipo da url for str
        return url.strip()
    else:
        return ''  # retorna str vazia, e o valida_url se vira com ela


def valida_url(self):
    if not self.url:    # if not self.url verifica com o bool, se a str é verdadeira ou falsa
                        # ou seja, uma str vazia, ou zero ou none, é falsa
        raise ValueError('A URL está vazia')'''

from string_em_python_url.extrator_url import *

# rodando com a URL com valor "None"
extrator_url = ExtratorURL(None)
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)