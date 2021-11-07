"""from random import randint
from time import sleep
jogadas = dict()
lista = []
print('Valores sorteados:')
for n in range(1, 5):
    jogadas['jogador'] = f'jogador{n}'
    jogadas['valor'] = randint(1, 6)
    lista.append(jogadas.copy())
    print(f'O {jogadas["jogador"]} tirou {jogadas["valor"]}')
    sleep(1)
# Todas as tentativas de fazer o Ranking dos jogadores falharam
"""
# Resolução da aula
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'    {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print(ranking)  # itens viram tuplas
print('-='*15)
print('-='*15)
print(' == RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
    print(f'  {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('-='*15)
