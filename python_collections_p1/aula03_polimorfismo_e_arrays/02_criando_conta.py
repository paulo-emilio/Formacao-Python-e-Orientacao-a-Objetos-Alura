from python_collections_p1.conta import *

conta1 = ContaCorrente(1)
conta1.deposita(1000)
print(conta1)

conta2 = ContaPoupanca(2)
conta2.deposita(1000)
print(conta2)

contas = [conta1, conta2]

for conta in contas:
    conta.passa_o_mes()  # duck typing
    print(f'Passando o mês para conta {conta._codigo}... {conta}')
