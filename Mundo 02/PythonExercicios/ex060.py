"""print('='*35)
print('===== CALCULADORA DE FATORIAL =====')
print('='*35)
num = int(input('Insira o número: '))
n = num
f = num - 1

while f != 0:
    if f != 0:
        n = n * f
        f -= 1
print('\n{}! = {}'.format(num, n))

for num in range(num-1):
    if f != 0:
        n = n * f
        f -= 1
print('\n{}! = {}'.format(num+2, n))
"""
# Resoluções da aula

"""
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
"""

#metodo tradcional
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)