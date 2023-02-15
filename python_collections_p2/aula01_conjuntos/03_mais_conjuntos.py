usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
# nos 2 (usamos o '&'
print(f'Quem está nos 2 conjuntos: {usuarios_machine_learning & usuarios_data_science}')
print(f'Usuário 15 fez os 2 cursos? {15 in usuarios_data_science & usuarios_machine_learning}')
# está no 1° e não está no 2º (usamos o '-')
print(f'Quem está no 1º e não no 2º: {usuarios_data_science - usuarios_machine_learning}')
print(f'Usuário 15 fez DS mas não fez ML? {15 in usuarios_data_science - usuarios_machine_learning}')
# 'ou exclusivo' - fez um ou o outro, mas não os 2 (usamos o '^')
print(f'Quem fez um OU outro: {usuarios_data_science ^ usuarios_machine_learning}')
print(f'Usuário 56 está em um OU outro? {56 in usuarios_data_science ^ usuarios_machine_learning}')




