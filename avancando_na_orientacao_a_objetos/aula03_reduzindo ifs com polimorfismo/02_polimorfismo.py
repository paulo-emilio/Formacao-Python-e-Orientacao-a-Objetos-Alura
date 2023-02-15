from avancando_na_orientacao_a_objetos.aula01_modelo import *

lotr = Filme('lord of the rings', 2001, 178)
lotr.dar_likes()
print(f'{lotr.nome} - {lotr.ano} - {lotr.duracao} - {lotr.likes}')

print('-'*60)

sandman = Serie('sandman', 2022, 1)
sandman.dar_likes()
sandman.dar_likes()
print(f' - {sandman.nome} - {sandman.ano} - {sandman.temporadas} - {sandman.likes}')


# imprimindo serie e filme, mesmo com seus atributos diferentes
filmes_e_series = [lotr, sandman]
for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(f'Nome: {programa.nome}\nAno: {programa.ano}\nLikes: {programa.likes}\n{detalhes}')