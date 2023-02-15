from datetime import datetime

# %A -> Dias da semana por extenso
# %d -> Dias do mês
# %m -> Meses em númerais
# %y -> Ano em 2 dígitos
# %Y -> Ano em 4 dígitos
# %H -> Hora em decimal
# %M -> Minuto em decimal
# %S -> Segundo em decimal

hoje = datetime.today()
hoje_format = hoje.strftime('%d/%m/%Y - %H:%M')
print(hoje_format)
print(type(hoje_format))  # hoje_format se transformou em str, ou seja,
                          # não podemos mais o usar, por exemplo: .weekend e .mouth
                          # Então: o .strtime() só deve ser usado para imprimir
