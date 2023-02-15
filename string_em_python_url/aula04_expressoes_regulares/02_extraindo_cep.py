endereco = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120'

import re  # Regular Expression -- RegEx

# CEP: 5 dígitos + hífen (opcional) + 3 dígitos

padrao_cep = re.compile('[0-9]{5}-?[0-9]{3}')
                                # '{5}' define quantas vezes esse grupo deve aparecer
                                    # '?' mostra que o grupo anterior ('-') pode aparecer uma ou nenhuma vez
                                    # também pode ser usado {0,1} na frente de '-'
                                        # '0-9' dígitos de 0 até 9
# '{}' pode ser usado com letras também, ex: {a-z}

busca = padrao_cep.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)
