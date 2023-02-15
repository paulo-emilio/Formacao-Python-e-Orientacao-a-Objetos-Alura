from avancando_na_orientacao_a_objetos.aula01_modelo import Filme

# foi criado a classe Programa em aula01_modelo para ser usada pelas
# classes: Filme e Serie

# Ocorreram problemas com as váriaveis, pois estao privadas
# e as classes filhas não conseguem acessar

#corrigido na aula 04_reutilizando_ainda_mais

batman = Filme('Batman', 2008, 160)
print(batman.nome)
