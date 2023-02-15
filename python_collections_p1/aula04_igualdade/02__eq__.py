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


class ContaMultiploSalario(ContaSalario):
    pass


conta1 = ContaSalario(69)
print(conta1)

conta2 = ContaSalario(69)
print(conta2)

print(conta1 == conta2) # retorna False antes de criarmos o __eq__ na classe
# por isso vamos criamos o __eq__ na classe ContaSalario:

'''
def __eq__(self,outro):
    return self._codigo == outro._codigo
'''

# validando se as contas são do mesmo tipo:
# caso exemplo: conta1 seja ContaSalário, e conta2 seja ContaCorrente
'''
def __eq__(self,outro):
    if type(outro) != ContaSalario:
        return False
    return self._codigo == outro._codigo
'''


conta3 = ContaSalario(10)
conta4 = ContaMultiploSalario(10)

# ContaMultiploSalario herda de ContaSalario, então também retorna True

print(conta3 == conta4)

# Um objeto do tipo filho (ContaMultiploSalario) é do tipo Mãe também (ContaSalario)