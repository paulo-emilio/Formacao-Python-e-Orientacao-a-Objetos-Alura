import re

# [] -> define um range ou grupo de caracteres                      // [0-9]; [a-z]; [abc]
#  * -> marca nenhuma, uma ou mais ocorrencias                      // sol*
# {} -> quantidade de repetições de uma ocorrência definida         // [abc]{5}
# \d -> qualquer número de 0 a 9                                    // \d{3,4}
# \w -> qualquer numero de 0 a 9, letra de A até Z, ou _(underline) // \w{10}
#  | -> um ou outro                                                 // @|$
# () -> captura e agrupa                                            // (\w{4})

'''padrao1 = '[0-9][a-z][0-9]'  # num - letra - num
texto1 = '123 1a2 1cc a11'
resposta1 = re.search(padrao1, texto1)
print(resposta1)
print(resposta1.group())  # somente o achado

padrao2 = '[0-9][a-z]{2}[0-9]'
texto2 = '123 1a2 1cc a11'
resposta2 = re.search(padrao2, texto2)
print(resposta2.group())  # erro pois nao existe isso'''

padrao_email = '\w{1,50}@\w{3,10}(.\w{2,3}){2}'
email1 = 'isso nao é parte do email = bbbsc3652@gmail.com.br//e nem isso'
resposta = re.search(padrao_email, email1)
print(resposta)
