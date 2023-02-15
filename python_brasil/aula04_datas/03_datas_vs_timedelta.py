from datetime import datetime, timedelta
from python_brasil.datas_br import DatasBr

hoje = datetime.today()
amanha = datetime.today() + timedelta(days=1, hours=1)  # timedelta define quantidades de tempo
                                                        # nesse exemplo estamos colocando amanha
                                                        # como sendo 1 dia e 1 hora depois de hoje
print(amanha - hoje)
print('*---'*30)

# o timedelta() pode ser usado na classe para testar o código:
cadastro = DatasBr()
print(cadastro.tempo_cadastro())
