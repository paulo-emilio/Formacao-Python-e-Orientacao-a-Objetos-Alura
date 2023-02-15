from python_brasil.cep_acesso import BuscaEndereco

cep = BuscaEndereco(35620000)
bairro, cidade, estado = cep.acessa_via_cep()  # criando váriaveis para cada valor na tupla criada
                                               # dentro do método 'acessa_via_cep()'

print(bairro, cidade, estado)
