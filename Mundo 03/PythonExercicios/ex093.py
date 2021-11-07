jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = list()
for c in range(partidas):
    gol = int(input(f'Quantos gols na partida {c}? '))
    gols.append(gol)
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('=' * 60)
print(jogador)
print('=' * 60)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=' * 60)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p, v in enumerate(gols):
    print(f'    => Na partida {p}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
