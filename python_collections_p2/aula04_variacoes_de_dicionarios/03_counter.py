from collections import defaultdict, Counter

meu_texto = 'Rock in Roll like in roll the Rock rock'.lower()

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1
print(aparicoes)

# Counter()
contador_aparicoes = Counter(meu_texto.split())  # conta as palavras e devolve um dict
print(contador_aparicoes)

print('~~'*50)


# exemplo de uso do defaultdict
class Conta:
    def __init__(self):
        print('Criando uma conta nova...')


contas = defaultdict(Conta)
print(contas[1])
print(contas[2])
print(contas[1])  # não cria mais, pois já existe uma conta com chave 1

print(contas)


