# from validate_docbr import CNPJ
# empresa_cnpj = CNPJ()
# ex_cnpj = '35379838000112'
# validacao = empresa_cnpj.validate(ex_cnpj)
# print(validacao)

# Criando os metodos do CNPJ dentro de cpf_cnpj

from python_brasil.cpf_cnpj import CpfCnpj

darth_cnpj = CpfCnpj(35379838000112, 'cnpj')
print(darth_cnpj)
