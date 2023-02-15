class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo


    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'Código: {self._codigo} -- Saldo: {self._saldo}'


conta1 = ContaSalario(1)
conta1.deposita(100)
conta2 = ContaSalario(69)
conta2.deposita(69)
conta3 = ContaSalario(182)
conta3.deposita(8)
contas = [conta1,conta2, conta3]

for conta in contas:
    print(conta)

'''sorted(contas)''' # não dá certo pois ele compara ContaSalario com ContaSalario


'''def extrai_saldo(conta):
    return conta._saldo

for conta in sorted(contas, key=extrai_saldo):
    print(conta)''' # muito ruim nem sei pra que ensinou

print('Ordenando por saldo')
from operator import attrgetter

for conta in sorted(contas, key=attrgetter('_saldo')):
    print(conta)

    # ruim tbm, vamos aprender na próxima aula ->