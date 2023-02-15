usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()  # cópia rasa da lista
assistiram.extend(usuarios_machine_learning)  # extendendo a lista
# agora 'usuarios_data_science' e 'usuarios_machine_learning' estão em 'assistiram'
# mas os que tem nos 2, ficaram repetidos -> [15, 23, 43, 56, 13, 23, 56, 42] 2x23 e 2x56
print(assistiram)

set_assistiram = set(assistiram)  # transforma em um CONJUNTO, tira os repetidos e coloca em ordem
print(f'set_assistiram: {set_assistiram}')
print('For/in set_assistiram')
for usuario in set_assistiram:
    print(usuario, end=' - ')
print('\n')
# ou seja, poderia ter criado já um conjunto:
'''
conjunto_assistiram = set(usuarios_machine_learning + usuarios_data_science)
print(f'conjunto_assistiram: {conjunto_assistiram}')
'''

# conjunto pode ser criando com chaves {}, ex:
conjunto_ex = {3, 8, 2, 3, 4, 5, 6}
# conjunto não possui ordem, não possui indexação, o que está dentro é aleatório
# conjunto_ex[3] -> não existe
print(conjunto_ex)

# também é possível criar dois conjuntos e junta-los:
print('\nJuntando 2 conjuntos:')
con_usuarios_data_science = {15, 23, 43, 56}
con_usuarios_machine_learning = {13, 23, 56, 42}
print(con_usuarios_machine_learning | con_usuarios_data_science)  # operação de 'OU' '|'
                                                                    # '|' contra-barra invertida
