def ficha(nome="desconhecido", gols=0):
    if nome == "":
        nome = 'desconhecido'
    # if gols is None:
        # gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


name = str(input('Nome do jogador: '))
gol = input('Número de gols: ')
if gol == '':
    gol = 0
else:
    gol = int(gol)
ficha(name, gol)

# Resolução da aula

def ficha(jog='<desconhecido', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)