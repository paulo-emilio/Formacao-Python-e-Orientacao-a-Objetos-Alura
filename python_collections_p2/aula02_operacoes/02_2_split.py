meu_texto = 'Olá mundo diga olá a todos nós querido mundo'
print(f'set meu_texto: \n{set(meu_texto)}')  # vira um conjunto das letras não repetidas

split_meu_texto = meu_texto.split()  # vira uma lista
print(f'\nsplit() de meu_texto: \n{split_meu_texto}')

conjunto_split_meu_texto = set(split_meu_texto)  # conjunto (sem repetição de palavras)
print(f'\nconjunto do split de meu_texto: \n{conjunto_split_meu_texto}')
