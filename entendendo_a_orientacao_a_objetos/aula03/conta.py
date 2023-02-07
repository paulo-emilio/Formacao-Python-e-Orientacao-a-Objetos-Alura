class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f'Contruindo Objeto ... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = Conta.codigo_banco()

    def extrato(self):
        print('-'*50)
        print('-- EXTRATO --')
        print(f'Titular: {self.__titular}\nSaldo: R${self.__saldo}')
        print('-'*50)

    def deposita(self, valor):
        print('-'*50)
        print(f'Depositando R${valor} reais na conta número {self.__numero}...')
        self.__saldo += valor
        print('-'*50)

    @property
    def __pode_sacar(self):
        return self.__saldo + self.__limite

    def saca(self, valor):
        print('-'*50)
        print(f'Sacando R${valor} reais na conta número {self.__numero}...')
        if valor <= self.__pode_sacar:
            self.__saldo -= valor
        else:
            print(f'LIMITE: Você não pode sacar este valor! Você pode sacar no máximo: R${self.__limite + self.__saldo}')
        print('-'*50)

    def tranfere(self, valor, destino):
        print('-'*50)
        print('<- TRANSFERINDO ->')
        if valor <= self.__pode_sacar:
            self.saca(valor)
            destino.deposita(valor)
        else:
            print('Você não possui limite suficiente')

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        print('Definindo novo limite...')
        self.__limite = novo_limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}



'''
from aula03.conta import Conta

conta1 = Conta(666, "Lúcifer", 666.0, 666.666)
conta2 = Conta(222, "Two", 222.0, 2000.0)
conta3 = Conta(333, "Trix", 333.0, 3000.0)

print('-'*10)

# Conta.extrato(conta1)

conta1.deposita(445.0)
conta1.extrato()
conta1.saca(445.0)
conta1.extrato()

'''