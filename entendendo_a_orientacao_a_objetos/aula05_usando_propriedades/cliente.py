class Cliente:
    def __init__(self, nome):
        self.__nome = nome
    @property
    def nome(self):
        print('Chamando property (get) nome() ...')
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print('Chamando (nome.setter) nome() ...')
        self.__nome = nome


    '''def get_nome(self, cliente):
        self.nome = self.nome.title()'''




# 04_propriedades_usando_cliente