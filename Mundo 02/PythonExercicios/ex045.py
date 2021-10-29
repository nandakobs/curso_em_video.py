"""from time import sleep
from random import randint
print('\033[1;33m=-'*12)
print('  JOKENPÔ - VOCÊ VS PC  ')
print('=-'*12)
print('Você consegue me vencer?')
user = int(input('Escolha: [1]Pedra  [2]Papel [3]Tesoura\n'))
pc = randint(1, 3)
#print(pc)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if user == 3 and pc == 2:
    print('\nTesoura corta o papel! Você venceu!')
elif pc == 3 and user == 2:
    print('\nTesoura corta o papel! Ganhei!')
elif user == 3 and pc == 1:
    print('\nPedra quebra a tesoura! Você venceu!')
elif pc == 3 and user == 1:
    print('\nPedra quebra a tesoura! Ganhei!')
elif user == 2 and pc == 1:
    print('\nPapel embrulha a pedra! Você venceu!')
elif pc == 2 and user == 1:
    print('\nPapel embrulha a pedra! Ganhei!')"""

# Resolução da aula
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:  # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:  # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')





