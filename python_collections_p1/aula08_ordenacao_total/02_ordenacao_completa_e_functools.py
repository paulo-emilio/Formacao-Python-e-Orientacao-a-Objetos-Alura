from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo

    def __lt__(self, other): # 'lesser than (menor que)'
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return  self._codigo < other._codigo


    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'Código: {self._codigo} -- Saldo: {self._saldo}'

# NOVO: _(se saldo igual, compara _codigo:
'''    
def __lt__(self, other): 
    if self._saldo != other._saldo:
        return self._saldo < other._saldo
    return  self._codigo < other._codigo'''

# <= e >= não está implementado, vamos implementar!
# antes da classe:
'''
from functools import total_ordering
@total_ordering
'''