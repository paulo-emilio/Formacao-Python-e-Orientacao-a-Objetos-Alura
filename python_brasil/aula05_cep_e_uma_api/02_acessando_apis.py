# Vamos utilizar a API "ViaCEP" do IBGE:
# ex: viacep.com.br/ws/01001000/json/

# Para acessar APIs utilizamos no Pyhton a biblioteca requests

from python_brasil.cep_acesso import BuscaEndereco

cep = BuscaEndereco(35620000)
print(cep.acessa_via_cep())


# foi criado
'''
    def acessa_via_cep(self):
        r = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/')
        return r.json()
'''


