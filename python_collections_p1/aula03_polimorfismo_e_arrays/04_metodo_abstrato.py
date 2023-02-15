# criando o método abstrato 'passa_mes' na classe 'Conta'
# para que todos que quiserem herdar dessa classe precisem
# implementar o método 'passa_mes'

# o que fiz:
# 1 - importei 'ABCMeta' e 'abstractmethod' de 'abc'
# 2 - defini a classe conta como abstrata, atravéz de 'metaclass=ABCMeta'
# 3 - criei o '@abstractmethod' 'passa_o_mes' dentro da classe Conta
"""from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):
    ...
    ...
    @abstractmethod
    def passa_o_mes(self):
        pass"""

# tentando instanciar a classe 'ContaInvestimento'
# da erro, pois ela não possui o método abstrato requerido
# pela classe 'Conta' da quão 'ContaInvestimento herda
from python_collections_p1.conta import *
ContaInvestimento(123)