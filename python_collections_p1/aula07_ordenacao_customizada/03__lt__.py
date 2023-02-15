class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo

    def __lt__(self, other): # 'lesser than (menor que)'
        return self._saldo < other._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'Código: {self._codigo} -- Saldo: {self._saldo}'

conta1 = ContaSalario(1)
conta1.deposita(100)
conta2 = ContaSalario(69)
conta2.deposita(8)
conta3 = ContaSalario(182)
conta3.deposita(66)
contas = [conta1,conta2, conta3]

print(conta2 < conta1)

for conta in sorted(contas):
    print(conta)