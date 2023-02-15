from avancando_na_orientacao_a_objetos.aula01_modelo import *

lotr = Filme('lord of the rings', 2001, 178)
lotr.dar_likes()

sandman = Serie('sandman', 2022, 1)
sandman.dar_likes()
sandman.dar_likes()

# foi criado dentro de cada classe o metodo:
'''def __str__(self):
        return f'Nome: {self.nome}\nAno: {self.ano}\n'Temporadas: {self.temporadas}\nLikes: {self.likes}'''
# esse método faz com que o print se transforme nele
# exemplo:
print(lotr)

Programa.linha()

filmes_e_programas = [lotr, sandman]

for programa in filmes_e_programas:
    print(programa)
    Programa.linha()
