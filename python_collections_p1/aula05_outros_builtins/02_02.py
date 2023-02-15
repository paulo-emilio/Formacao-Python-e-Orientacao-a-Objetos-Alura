nomes=[('Paulo', 22, 2000),
       ('Darth', 80, 9898),
       ('L0K1', 3, 2020)]

print('Desenpacotamento direto:')
'''
for nome, idade, nascimento in nomes:  # desenpacotando nome
    print(nome)
'''
for nome, _, _ in nomes:  # desenpacotando nome, ignorando o resto com underline
    print(nome)