from python_brasil.datas_br import DatasBr
# from _datetime import datetime
# print(datetime.today())

cadastro = DatasBr()
print(cadastro.momento_cadastro)
print(f'{cadastro.mes_cadastro()} / {cadastro.dia_semana()}')
