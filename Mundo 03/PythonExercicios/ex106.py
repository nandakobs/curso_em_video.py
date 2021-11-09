"""def busca():
    while True:
        cmd = input('Função ou Biblioteca >')
        textao = """ """
        textao = help(cmd)
        print(f'\033[7;49;39m{textao}\033[m')
        if cmd in "FIMfim":
            break

def linhas_brancas(msg):
    print('\033[7;49;39m', '~' *40, '\033[m')
    print(f'\033[7;49;39m', f'{msg:^40}', '\033[m')
    print('\033[7;49;39m', '~' * 40, '\033[m')

def fundo_branco(msg):
    print('\033[7;49;39m', help(cmd), '\033[m')

linhas_brancas('SISTEMA DE AJUDA PYHELP')
busca()"""

# Resolução da aula
from time import sleep
c =('\033[m',           # 0 - SEM CORES
    '\033[0;30;41m',    # 1 - VERMELHO
    '\033[0;30;42m',    # 2 - VERDE
    '\033[0;30;43m',    # 3 - AMARELO
    '\033[0;30;44m',    # 4 - AZUL
    '\033[0;30;45m',    # 5 - ROXO
    '\033[7;30m'        # 6 - BRANCO
    )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)



