class ContaCorrente:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'[>> Código: {self._codigo} -- Saldo: ${self._saldo} <<]'


conta_paulo = ContaCorrente(42)
print(conta_paulo)
conta_paulo.deposita(666)
print(conta_paulo)

conta_flavia = ContaCorrente(22)
conta_flavia.deposita(1000000 )
print(conta_flavia)

print('-'*60)

contas = [conta_paulo, conta_flavia]
print(contas)
for conta in contas:
    print(conta)