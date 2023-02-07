def cria_conta(num, titular, saldo, limite):
    conta = {"Numero": num, "Titular": titular, "Saldo": saldo, "Limite": limite}
    return conta


def deposita(conta, valor):
    conta["Saldo"] += valor

def saca(conta, valor):
    conta["Saldo"] -= valor

def extrato(conta):
    print(f'Saldo: {conta["Saldo"]}')