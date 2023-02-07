from entendendo_a_orientacao_a_objetos.aula03.conta import Conta
# criando codigo do banco
'''@property    
    def codigo_banco(self):
        return self.__codigo_banco'''
conta1 = Conta(666, "Lúcifer", 666.0, 666.666)
print(f'Código do Banco da conta de {conta1.titular}: {conta1.codigo_banco()}')

# o código do banco deve poder ser acessado mesmo sem nenhum objeto criado
# então usamos o @staticmethod
'''@staticmethod   
    def codigo_banco():
        return "001"'''

# mais exemplo: poderia ser criado o codigos_bancos()
'''@staticmethod
def codigos_bancos():
    return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}'''

codigos = Conta.codigos_bancos()
print(codigos)
print(codigos['BB'])
print(codigos['Caixa'])

