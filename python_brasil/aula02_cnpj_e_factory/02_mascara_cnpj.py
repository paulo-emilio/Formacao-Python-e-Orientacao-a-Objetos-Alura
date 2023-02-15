# eu já tinha feito a máscara
# mas vamos testar tudo:
from python_brasil.cpf_cnpj import CpfCnpj

darth_cnpj = CpfCnpj(35379838000112, 'cnpj')
print(darth_cnpj)

darth_cpf = CpfCnpj(32007832062, 'cpf')
print(darth_cpf)
