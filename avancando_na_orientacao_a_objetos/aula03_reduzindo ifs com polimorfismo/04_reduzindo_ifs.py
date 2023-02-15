from avancando_na_orientacao_a_objetos.aula01_modelo import *

lotr = Filme('lord of the rings', 2001, 178)
lotr.dar_likes()
print('-'*60)

sandman = Serie('sandman', 2022, 1)
sandman.dar_likes()
sandman.dar_likes()

filmes_e_programas = [lotr, sandman]

# criando a def 'imprime'
'''def imprime(self):
        print(f'Nome: {self.nome}\nAno: {self.ano}\nLikes: {self.likes}')
'''
for programas in filmes_e_programas:
    programas.imprime()
    print('-'*40)

 # ainda assim não conseguimos imprimir os diferentes atributos que cada classe possui
 # então vamos criar um imprime para casa classe