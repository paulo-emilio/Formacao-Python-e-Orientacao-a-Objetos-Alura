# criando class Documento e separando a classe CpfCnpj

from python_brasil.cpf_cnpj import Documento

cpf1 = Documento.cria_documento(32007832062)

cnpj1 = Documento.cria_documento(35379838000112)

print(f'CPF : {cpf1}')

print(f'CNPJ: {cnpj1}')
