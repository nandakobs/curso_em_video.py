# 6 palpites por jogo, entre 1 e 60
from random import randint
from time import sleep
print('='*45)
print('{:^45}'.format(' JOGA NA MEGA SENA '))
print('='*45)
n = int(input('Quantos jogos você quer que eu sorteie? ').strip())
lista = []
print(f'=-=-=-=-=-=-= SORTEANDO {n} JOGOS =-=-=-=-=-=-=')
for c in range(n):
    lista.append([randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)])
    sleep(1)
    print(f'Jogo {c+1}: {lista[c]}')
print(f'=-=-=-=-=-=-= <<< BOA SORTE! >>> =-=-=-=-=-=-=')

"""
# Resolução da aula
from random import randint
from time import  sleep
lista = list()
jogos = list()
print('-' * 30)
print('      JOGA NA MEGA SENA        ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <=quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)"""

