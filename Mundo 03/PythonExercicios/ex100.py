from random import randint
from time import sleep


def sorteia(valor):
    print('Sorteando 5 valores na lista: ', end=' ')
    for val in range(5):
        numeros.append(randint(0, 100))
        print(numeros[val], end=' ')
        sleep(0.5)
    print(' PRONTO!')


def soma_par(val):
    par = list()
    for val in numeros:
        if val % 2 == 0:
            par.append(val)
    print(f'Somando os valores pares de {numeros}, temos {sum(par)}')


numeros = list()
soma_par(sorteia(numeros))
