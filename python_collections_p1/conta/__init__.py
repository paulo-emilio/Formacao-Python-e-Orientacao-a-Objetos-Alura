from abc import ABCMeta, abstractmethod
from functools import total_ordering

@total_ordering
class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != Conta:
            return False
        return self._codigo == outro._codigo

    def __lt__(self, other):  # 'lesser than' (menor que)
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo

    @abstractmethod
    def passa_o_mes(self):
        pass

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'[>> Código: {self._codigo} -- Saldo: ${self._saldo} <<]'


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass
