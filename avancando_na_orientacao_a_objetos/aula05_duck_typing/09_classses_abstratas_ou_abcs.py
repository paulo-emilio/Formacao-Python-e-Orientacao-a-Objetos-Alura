# from abc import ABC # abstract base classes

# importando MutableSequence, nao roda pq nao usei todos os métodos que ela possui
from collections.abc import MutableSequence

class Playlist(MutableSequence):
    pass

filmes = Playlist()

from numbers import Complex
class Numero(Complex):
    def __getitem__(self, item):
        super().__bool__()  # apesar de normalmente classes abstratas nao possuirem implementação,
        # no Python elas podem possuir, podemos descobrir clicando no nome da classe segurando o Ctrl
num = Numero()