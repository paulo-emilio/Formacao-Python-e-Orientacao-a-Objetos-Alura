import re


class TelefonesBr:
    def __init__(self, num):
        if self.valida_telefone(num):
            self.telefone = num
        else:
            raise ValueError('Número incorreto!')

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, num):
        padrao = '([0-9]{2,3}?)?([1-9]{2})([6-9])?([0-9]{4})([0-9]{4})'
        resposta = re.findall(padrao, num)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao = '([0-9]{2,3}?)?([1-9]{2})([6-9])?([0-9]{4})([0-9]{4})'
        resposta = re.search(padrao, self.telefone)
        num_formatado = f'+{resposta.group(1)} ({resposta.group(2)}) ' \
                        f'{resposta.group(3)} {resposta.group(4)}-{resposta.group(5)}'
        return num_formatado



