"""from random import randint
num = randint(0, 5)
res = int(input('Digite um numero entre 0 e 5: '))
if res == num:
    print('Você adivinhou!')
else:
    print('Você perdeu! O numero secreto era {}'.format(num))
"""
# A Resolução da aula
from random import randint
from time import sleep #faz com q o computador dê uma pausa
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2) #()segundos
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))

