class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
        self.linha = '-'*80
        
    def dar_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title().strip()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'   {self.nome} / {self.ano} / ' \
               f'{self.duracao} min / Likes: {self.likes}\n{self.linha}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'   {self.nome} / {self.ano} / ' \
               f'{self.temporadas} temporadas / Likes: {self.likes}\n{self.linha}' \


class Playlist:
    def __init__(self, nome,programas):
        self.nome = nome
        print(f'\nPLAYLIST: {self.nome}')
        print('=-'*40)
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)




















'''
# running

lotr = Filme('lord of the rings: the fellowship of the ring', 2001, 178)
lotr.dar_likes()
print(f'FILME\nNome: {lotr.nome}\nAno: {lotr.ano}\nDuração: {lotr.duracao}\nLikes: {lotr.likes}')

print('-'*60)

sandman = Serie('sandman', 2022, 1)
print(f'SERIE\nNome: {sandman.nome}\nAno: {sandman.ano}\nDuração: {sandman.temporadas}\nLikes: {sandman.likes}')

# setter de nome (@nome.setter)
sandman.nome = 'game of thrones'
print(f'SERIE\nNome: {sandman.nome}\nAno: {sandman.ano}\nDuração: {sandman.temporadas}\nLikes: {sandman.likes}')
'''