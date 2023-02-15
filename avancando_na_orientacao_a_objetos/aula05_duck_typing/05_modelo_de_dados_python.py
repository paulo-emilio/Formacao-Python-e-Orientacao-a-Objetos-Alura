from avancando_na_orientacao_a_objetos.aula01_modelo import *
# criando o duck typing 'len' dentro de Playlist
'''    def __len__(self):
        return len(self._programas)'''

lotr = Filme('lord of the rings', 2001, 178)
starwars = Filme('Star Wars', 1990, 180)
got = Serie('Game of Thrones', 2012, 8)
bb = Serie('Breaking Bad', 2010, 5)

lotr.dar_likes(); lotr.dar_likes(); lotr.dar_likes(); lotr.dar_likes()
starwars.dar_likes(); starwars.dar_likes()
got.dar_likes(); got.dar_likes()
bb.dar_likes(); bb.dar_likes(); bb.dar_likes()

filmes_e_series = [lotr, got, bb]
playlist_fds = Playlist('Fim de Semana', filmes_e_series)

print(f'Tamanho da Playlist "{playlist_fds.nome}": {len(playlist_fds)}')

