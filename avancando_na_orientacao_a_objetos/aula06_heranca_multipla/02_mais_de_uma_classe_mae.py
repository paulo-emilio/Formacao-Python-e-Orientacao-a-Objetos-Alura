from avancando_na_orientacao_a_objetos.aula06_heranca_multipla import *


paulo = Junior()
'''paulo.busca_cursos_do_mes''' # paulo é da classe Junior, entao só acessa da classe Alura
paulo.busca_perguntas_sem_resposta()
paulo.registra_horas(8)
paulo.mostrar_tarefas()

print('-'*50)
# emilio é da classe Pleno, entao acessa de Alura e Caelum
emilio = Pleno()
emilio.busca_perguntas_sem_resposta()
emilio.busca_cursos_do_mes()
# o mostrar tarefas de emilio pega o mostrar tarefas de alura, mas ele é dos dois...
emilio.mostrar_tarefas()

# segue em 04_resolucao_de_metodos

