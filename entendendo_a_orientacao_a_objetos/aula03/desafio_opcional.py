class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


    def formata(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')







# from datas import Data
#d = Data(21,11,2007)
#d.formata()