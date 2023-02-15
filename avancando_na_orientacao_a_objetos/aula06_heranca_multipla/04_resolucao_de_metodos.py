from avancando_na_orientacao_a_objetos.aula06_heranca_multipla import *
paulo = Junior()
emilio = Pleno()

# o mostrar tarefas de emilio pega o mostrar tarefas de alura, mas ele é dos dois...
emilio.mostrar_tarefas()

# como funciona isso:
# o Python 3 procura o método na próprima classe, depois na primeira classe mãe
# depois na classe vó (mesmo tendo outra classe mãe), e só ai volta na outra mãe:
# Algorítimo usado pelo Python 3 = MRO
# Pleno() > Alura() > Funcionario() > Caelum() > Funcionario()
# MAS, o MRO verifica se há repetições, no caso SIM (Funcionario())
# e sabendo que é repetida ele verifica se existe alguma "Good Head"
# Good head -> verificada se existe alguma classe abaixo de Funcionario() que possa
# ser utilizada, no caso SIM, a classe Caelum
# e nesse caso a ordem fica assim: Pleno() > Alura() > Caelum() > Funcionario()