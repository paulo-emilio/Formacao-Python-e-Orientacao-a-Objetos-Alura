aparicoes = {'Paulo': 1,
             'Rock': 2,
             'Darth': 2,
             'L0K1': 1}  # O 1º elemento é a chave

print(aparicoes['Paulo'])  # 1

# criando pelo Construtor
aparicoes_construtor = dict(Paulo=1, Rock=2)
print(aparicoes_construtor)

# get (verifica se tem essa chave no dicionario
print('\nGet:')
print(f'"Bolacha" está em aparicoes? {aparicoes.get("Bolacha", 0)}')  # se não tiver devolve 0
print(f"'Rock' está em aparicoes? {aparicoes.get('Rock')}") # 1
