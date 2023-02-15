import re
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')
        else:
            padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
            match = padrao_url.match(self.url)
            if not match:
                raise ValueError('URL não é válida')

    def index_url_interrogacao(self):
        return self.url.find('?')

    def get_url_base(self):
        return self.url[:self.index_url_interrogacao()]

    def get_url_parametros(self):
        return self.url[self.index_url_interrogacao()+1:]

    def get_valor_parametro(self, parametro_busca):
        index_parametro_busca = self.get_url_parametros().find(parametro_busca)
        index_valor = index_parametro_busca + len(parametro_busca) + 1
        index_e_comercial = self.get_url_parametros().find('&', index_valor)
        if index_e_comercial == -1:
            valor = self.get_url_parametros()[index_valor:]
        else:
            valor = self.get_url_parametros()[index_valor:index_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\nParâmetros: ' + self.get_url_parametros() + \
            '\nBase: ' + self.get_url_base()

    def __eq__(self, other):
        return self.url == other





