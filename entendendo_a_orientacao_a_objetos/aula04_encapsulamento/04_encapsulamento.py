from entendendo_a_orientacao_a_objetos.aula03.conta import Conta

conta1 = Conta(666, "Lúcifer", 666.0, 666666666.666)
conta2 = Conta(222, "Two", 222.0, 2000.0)
conta3 = Conta(333, "Trix", 333.0, 3000.0)

# transferência
valor = 10
# saca
conta2.saca(100)
conta2.extrato()
# deposita
conta3.deposita(100)
conta3.extrato()

# transferencia certa
conta3.tranfere(100, conta2)
conta3.extrato()
conta2.extrato()
