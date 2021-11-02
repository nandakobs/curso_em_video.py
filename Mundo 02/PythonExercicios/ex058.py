from colorama import init, Fore
from random import randint
from time import sleep
init()
computador = randint(0, 10)
print(Fore.GREEN, '-=-' * 20)
print(Fore.CYAN, 'Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print(Fore.GREEN, '-=-' * 20)
jogador = int(input('\033[36mEm que número eu pensei?\033[m '))
print(Fore.CYAN, '\nDeixa eu ver...')
sleep(0.5)
vezes = 1
while jogador != computador:
    print(Fore.LIGHTRED_EX,'Huum, não foi bem esse. Vou te dar mais uma chance!')
    jogador = int(input('\033[36mEm que número eu pensei?\033[m '))
    print(Fore.CYAN, '\nDeixa eu ver...')
    sleep(0.5)
    vezes += 1
if vezes == 1:
    print(Fore.GREEN, 'PARABÉNS! Você conseguiu me vencer na 1ª tentativa!')
else:
    print(Fore.LIGHTGREEN_EX, 'IRRRAA! Tu conseguiu acertar depois de {} palpites.'.format(vezes))


"""
# Resolução da aula

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
"""