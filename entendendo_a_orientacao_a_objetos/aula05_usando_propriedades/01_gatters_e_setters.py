from entendendo_a_orientacao_a_objetos.aula03.conta import Conta
conta1 = Conta(666, "Lúcifer", 666.0, 666.666)
conta2 = Conta(222, "Two", 222.0, 2000.0)
conta3 = Conta(333, "Trix", 333.0, 3000.0)
print('-'*80)
# Criando os métodos para retornar (get) dados em conta.Conta
# get é o padrão usado para esse tipo de método

print(f'Saldo: {conta1.get_saldo()}')
print(f'Titular: {conta1.get_titular()}')
print(f'Limite: {conta1.get_limite()}')
conta1.set_limite(input("Definir limite para: "))
print(f'Limite: {conta1.get_limite()}')

