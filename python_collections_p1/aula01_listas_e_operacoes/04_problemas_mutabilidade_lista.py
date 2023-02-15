def faz_processamento_de_vizualizacao(lista):
    return len(lista)

idades = [12,65,44,33,98]
print(faz_processamento_de_vizualizacao(idades))

# FICAR ATENTO COM OS MÉTODOS, O MÉTODO PODE SER ALTERADO, POR EXEMPLO PARA ADD OUTRO VALOR
# À LISTA, ASSIM MUDANDO MINHA LISTA, SENDO QUE EU QUERIA SÓ SABER SEU TAMANHO

# Se eu quiser que meu parâmetro seja opcional:
# dessa forma a 'lista = []', a lista vazia será criada da primeira vez q for chamada,
# mas o problema é, das próximas vezes que for chamada, continuará usando essa lista
'''
def faz_processamento_de_vizualizacao(lista = []):
    return len(lista)
'''
# o cerreto seria:
'''
def faz_processamento_de_vizualizacao(lista = None):
    if lista == None:
        lista = []
    return len(lista)'''
