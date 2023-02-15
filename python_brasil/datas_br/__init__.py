from datetime import datetime


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                        'Julho', 'Agosto', 'Setembro', 'Outrubro', 'Novembro', 'Dezembro']
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro-1]

    def dia_semana(self):
        dias_da_semana = 'Segunda-feira', 'Terça-feira', 'Quarta-feira', \
            'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo'
        dia_semana = self.momento_cadastro.weekday()
        return dias_da_semana[dia_semana]

    def format_data(self):
        return self.momento_cadastro.strftime('%d/%m/%Y - %H:%M')

    def tempo_cadastro(self):
        return datetime.today() - self.momento_cadastro





