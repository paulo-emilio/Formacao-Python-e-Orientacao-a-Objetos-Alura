# VALIDANDO (somente quantidade):
# cpf_cnpj = 12345678901
# cpf_cnpj = str(cpf_cnpj)
# tamanho_cpf = len(cpf_cnpj)
# print(tamanho_cpf)

# FATIANDO:
# cpf_cnpj = 12345678901
# cpf_cnpj = str(cpf_cnpj)
# fatia_1 = cpf_cnpj[:3]
# fatia_2 = cpf_cnpj[3:6]
# fatia_3 = cpf_cnpj[6:9]
# fatia_4 = cpf_cnpj[9:]
# cpf_formatado = f'{fatia_1}.{fatia_2}.{fatia_3}-{fatia_4}'
# print(cpf_formatado)

from python_brasil.cpf_cnpj import CpfCnpj

cpf_darth = CpfCnpj(54671486130, 'cpf')

print(cpf_darth)

