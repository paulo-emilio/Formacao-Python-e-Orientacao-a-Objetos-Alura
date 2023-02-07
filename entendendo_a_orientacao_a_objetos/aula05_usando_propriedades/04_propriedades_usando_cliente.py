from cliente import Cliente

cliente1 = Cliente(input('Nome: '))
print(cliente1.nome)

# usando o setter
cliente1.nome = input('Novo nome: ')
print(cliente1.nome)



'''cliente1.get_nome(cliente1)
print(cliente1.nome)'''
