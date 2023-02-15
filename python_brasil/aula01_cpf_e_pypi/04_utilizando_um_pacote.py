# importando validate_docbr / CPF para o pacote 'CPF' criado nas primeiras aulas
from python_brasil.cpf_cnpj import CpfCnpj

cpf_darth = CpfCnpj('54671486130', 'cpf')  # true


# Substituindo o meu 'format_cpf' por .mask do pacote validate_docbr

cpf_darth.format_cpf()

print(cpf_darth)
