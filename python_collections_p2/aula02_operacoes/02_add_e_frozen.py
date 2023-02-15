usuarios = {1, 5, 76, 34, 52, 13, 17}
print(usuarios)
print(f'Tamanho: {len(usuarios)}')
# adicionando no conjunto ('add'):
print('\nAdd 13...')
print(usuarios)
usuarios.add(13)  # não add pq o 13 já está lá
print(f'Tamanho: {len(usuarios)}')
print('\nAdd 765...')
usuarios.add(765)
print(usuarios)
print(f'Tamanho: {len(usuarios)}\n')
print('~~'*50)

# Fazendo o conjunto ficar imutável (Congelar):
usuarios = frozenset(usuarios)
print(usuarios)

