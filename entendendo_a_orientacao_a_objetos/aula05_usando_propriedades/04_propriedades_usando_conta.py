from entendendo_a_orientacao_a_objetos.aula03.conta import Conta

conta1 = Conta(666, "Lúcifer", 666.666, 696969.69)
print(f'Limite de {conta1.titular}: {conta1.limite}')

conta1.limite = input('Novo limite: ')
print(f'Limite de {conta1.titular}: {conta1.limite}')
