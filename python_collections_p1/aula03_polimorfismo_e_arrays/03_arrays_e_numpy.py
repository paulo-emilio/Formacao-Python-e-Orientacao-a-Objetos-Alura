# Arrays são muito pouco utilizadas em Pyhton
# Normalmente vamos utilizar tuplas e listas
# Arrays são muito específicos

import array as arr

array_do_python = arr.array('d', [1,3.5]) # impossível colocar um str na lista nesse caso

print(array_do_python)

print('-'*60)
'''-----------------------------------------------------------------------------------------'''

# numpy -> usado para quando muita matemática (Data Science)
import numpy as np
teste_numpy = np.array([1, 3.5])
print(teste_numpy)

teste_numpy += 3  #soma em todos números
print(teste_numpy)
