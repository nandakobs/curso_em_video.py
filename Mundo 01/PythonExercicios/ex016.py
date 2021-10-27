import math
num_real = float(input('Digite um numero real: '))
num_int = math.trunc(num_real)
print('O número {} tem a parte inteira {}.'.format(num_real, num_int))

"""
Resoluções da aula:

from math import trunc
num_real = float(input('Digite um numero real: '))
print('O número {} tem a parte inteira {}.'.format(num_real, trunc(num_real)))

num_real =  float(input('Digite um numero real'))
print('O numero {} tem a parte inteira {}.'.format(num_real, int(num_real)))
"""