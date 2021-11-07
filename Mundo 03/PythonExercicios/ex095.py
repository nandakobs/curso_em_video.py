jogadores = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(partidas):
        gol = int(input(f'Quantos gols na partida {c}? '))
        gols.append(gol)
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols[:])
    gols.clear()
    jogadores.append(jogador.copy())
    jogador.clear()
    continua = ''
    while 'S' != continua != 'N':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('=' * 30)
    if continua == 'N':
        break
print('-=' * 30)
print(f'{"cod":<4}{"nome":<20}{"gols":<20}{"total":<5}')
print('=' * 30)
for k, v in enumerate(jogadores):
    print(f'{k} {v["nome"]}{" ":^5}{v["gols"]}{" ":^5}{v["total"]}')
    # print("{:<4}{:<20}{:<20}{:<5}".format(k, v['nome'], v['gols'], v['total']))
# print(jogadores)
# jogadores = [{'nome': 'Ferfer', 'gols': [2, 1], 'total': 3}, {'nome': 'Marta', 'gols': [4, 4, 3], 'total': 11}, {'nome': 'Poode', 'gols': [0, 1], 'total': 1}]
print('=' * 30)
while True:
    mostra = int(input('Mostrar dados de qual jogador? '))
    if mostra == 999:
        print(f'<< VOLTE SEMPRE >>')
        break
    elif mostra > len(jogadores) - 1:
        print(f'ERRO! Não existe jogador com código {mostra}! Tente novamente.')
    elif mostra <= len(jogadores) - 1:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[mostra]["nome"]}:')
        for k, v in enumerate(jogadores[mostra]['gols']):
            print(f'    No jogo {k+1} fez {v} gols.')
    print('=' * 30)
