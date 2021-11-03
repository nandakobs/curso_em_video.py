from random import randint
lista = []
for nums in range(5):
    nums = randint(0, 100)
    lista.append(nums)
tupla = (lista[0], lista[1], lista[2], lista[3], lista[4])
print(f'Os valores sorteados foram {tupla}')
print(f'O menor valor da tupla é {min(tupla)} e o maior valor é {max(tupla)}.')

"""
# Resolução da aula
from random import randint
numeros =(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end='')
print(f'O menor valor da tupla é {min(tupla)}\nE o maior valor é {max(tupla)}.')
"""