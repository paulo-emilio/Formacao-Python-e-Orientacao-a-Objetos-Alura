idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
    print(f'| {i} - {idades[i]}', end= ' ')

# enumerate a partir de lista
print(f'\n\nLista com Enumerate: \n{list(enumerate(idades))}')

# enumerate a partir de for/in
print('\nFor/in com Enumerate: ')

for c in enumerate(idades):
    print(c, end= '  ')

print('\n\nFormatado:')
for i, idade in enumerate(idades):
    print(f'| {i} - {idade} ', end='')

