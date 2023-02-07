from entendendo_a_orientacao_a_objetos.aula03.conta import Conta
# criando limite para o saque em aula03.conta
'''        if valor <= self.saldo + self.limite:
            self.__saldo -= valor
        else:
            print(f'ERRO: Você não pode sacar este valor! Você pode sacar no máximo: R${self.__limite + self.__saldo}')
        print('-'*50)'''


conta1 = Conta(666, "Lúcifer", 10.0, 100.0)
print(f'Saldo: {conta1.saldo}')

conta1.saca(10)
print(f'Saldo: {conta1.saldo}')

# criando metodo pode_sacar
'''@property
    def pode_sacar(self):
        return self.__saldo + self.__limite'''
# colocando privado o método, para so ser acessado por outro método
'''def __pode_sacar(self):'''
