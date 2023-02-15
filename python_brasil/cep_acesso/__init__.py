import requests


class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep).replace('-', '').replace(' ', '')
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError('Número de caracteres Incorreto!')

    def __str__(self):
        return self.format_cep()

    def acessa_via_cep(self):
        r = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/')
        dados = r.json()
        return dados['bairro'], dados['localidade'], dados['uf']  # retorna uma tupla com esses dados

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'
