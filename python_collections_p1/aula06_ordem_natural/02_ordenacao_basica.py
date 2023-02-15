idades = [87, 15, 32, 65, 56, 32, 49, 37]
nomes=[('Paulo', 22, 2000),
       ('Darth', 80, 9898),
       ('L0K1', 3, 2020)]
print(f'Idades: {idades}')
sorted_id = sorted(idades)
print(f'Sorted: {sorted_id}')

reversed_id = list(reversed(idades)) # de trás pra frente
print(f'Reversed: {reversed_id}')

sorted_reverse = (sorted(idades, reverse=True))
print(f'Sorted Reverse = True: {sorted_reverse}')

# a lista não mudou:
print(f'\nA lista não mudou: {idades}')
# mudando a lista:
idades.sort()
print(f'Agora mudou com o sort(): {idades}')