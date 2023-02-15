aparicoes = {'Paulo': 1,
             'Rock': 2,
             'Darth': 2,
             'L0K1': 1}
print(aparicoes)
# adicionando ao dicionario
aparicoes['Sauron'] = 3
print(aparicoes)
# deletando
del aparicoes['Sauron']
print(aparicoes)

print(f'\nSauron está em aparições? {"Sauron" in aparicoes}')

print('\nfor/in: ')
for elemento in aparicoes.keys():  # caso for imprimir chaves, não é necessário o .keys()
    print(elemento, end=' ')

print('\n\nfor/in aparicoes.values:')
for elemento in aparicoes.values():
    print(elemento, end=' ')

print('\n\nfor/in elemento e apaicoes[elemento]:')
for elemento in aparicoes:
    valor = aparicoes[elemento]
    print(elemento, valor, end=' / ')

print('\n\nfor/in aparicoes.items:')
for elemento in aparicoes.items():
    print(elemento, end=' ')
# obs: cada dupla é uma tupla de tamanho 2

print('\n\nfor chave, valor in aparicoes:')
for chave, valor in aparicoes.items():
    print(f'chave {chave} tem valor {valor}')

print('\nlist de aparicoes adionando "Nome:" antes:')
# list compreenshion no dicionario
list_aparicoes = [f'Nome: {chave}' for chave in aparicoes]
print(list_aparicoes)
