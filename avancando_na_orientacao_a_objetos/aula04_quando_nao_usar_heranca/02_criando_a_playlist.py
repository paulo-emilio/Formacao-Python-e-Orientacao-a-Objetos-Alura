from avancando_na_orientacao_a_objetos.aula01_modelo import *

# foi criada a classe Playlist e aula01_modelo

lotr = Filme('lord of the rings', 2001, 178)
starwars = Filme('Star Wars', 1990, 180)
batman = Filme('Batman', 2014, 150)
sandman = Serie('sandman', 2022, 1)
got = Serie('Game of Thrones', 2012, 8)
bb = Serie('Breaking Bad', 2010, 5)

lotr.dar_likes(); lotr.dar_likes(); lotr.dar_likes(); lotr.dar_likes()
starwars.dar_likes(); starwars.dar_likes()
batman.dar_likes(); batman.dar_likes(); batman.dar_likes()
got.dar_likes(); got.dar_likes()
bb.dar_likes(); bb.dar_likes(); bb.dar_likes()
sandman.dar_likes(); sandman.dar_likes()

filmes_e_series = [lotr, batman, got, bb, sandman]
playlist_fds = Playlist('Fim de Semana', filmes_e_series)

# importei a classe mãe list (ja inclusa no python) para usála dentro de Playlist
'''class Playlist(list):
    def __init__(self, nome,programas):
        self.nome = nome
        print(f'\nPLAYLIST: {self.nome}')
        print('=-'*40)
        super().__init__(programas)'''

for programas in playlist_fds:
    print(programas)

print(f'Tamanho da Playlist: {len(playlist_fds)}')

print(f'{starwars.nome} está na playlist "{playlist_fds.nome}"? {starwars in playlist_fds}')