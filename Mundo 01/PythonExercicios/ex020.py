import random
alunas = input('Nomes das alunas: ').split(', ')
sorteado = random.sample(alunas, len(alunas))
print("A ordem de apresentação será: {}".format(sorteado))

"""
Resolução da aula:

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
"""