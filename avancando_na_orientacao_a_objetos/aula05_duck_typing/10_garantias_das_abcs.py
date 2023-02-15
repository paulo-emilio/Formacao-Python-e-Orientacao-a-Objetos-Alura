from collections.abc import Sized

class Listagem(Sized):
    def __init__(self, desc):
        self.desc = desc

    def __str__(self):
        return self.desc

    def __len__(self):
        return len(self.desc)

lista = Listagem('Nova_lista')
print(lista)