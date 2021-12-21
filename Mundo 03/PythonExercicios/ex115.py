def g(txt):
    """
    Deixa texto verde. G de green.
    """
    return f"\033[32m{txt}\033[m"


def b(txt):
    """
    Deixa texto azul. B de blue.
    """
    return f"\033[34m{txt}\033[m"


def r(txt):
    """
    Deixa texto vermelho. R de red.
    """
    return f"\033[31m{txt}\033[m"


def titulo(msg):
    print('-' * 40)
    print('{:^40}'.format(f"{msg}"))
    print('-' * 40)


def menu():
    titulo('MENU PRINCIPAL')
    print(f'{g(1)} - {b("Ver pessoas cadastradas")}\n'
          f'{g(2)} - {b("Cadastrar novas Pessoas")}\n'
          f'{g(3)} - {b("Sair do Sistema")}')
    print('-' * 40)
    op = 0
    while op not in (1, 2, 3):
        try:
            op = int(input(g('Sua opção: ')))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(r('ERRO! Por favor, digite uma opção válida!'))
        else:
            if op not in (1, 2, 3):
                print(r('ERRO! Por favor, digite uma opção válida!'))
    return op



def cadastrar():
    titulo('CADASTRO')
    nome = str(input('Nome: ')).strip()
    while True:
        try:
            idade = int(input('Idade: '))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(r('ERRO! Por favor, digite um numero inteiro válido!'))
        else:
            break
    print(f'Novo registro de {nome} adicionado.')
    cad_unico[f'{nome}'] = idade
    a = open('lista_ex115.txt', 'a')
    a.write(f"{nome}: {idade},\n")
    a.close()


def cadastradas():
    titulo('PESSOAS CADASTRADAS')
    for k, v in cad_unico.items():  # dicionario que é momentaneamente preenchido
       print(f'{k:<28}\t{v} anos')
    a = open('lista_ex115.txt', 'rt')  # texto arquivado
    lendo = a.read()
    print(lendo)


from time import sleep

cad_unico = dict()
while True:
    sleep(0.3)
    start = menu()
    if start == 1:
        sleep(0.3)
        cadastradas()
        # print(cad_unico)
    elif start == 2:
        sleep(0.3)
        cadastrar()
    else:
        sleep(1)
        titulo('PROGRAMA ENCERRADO, VOLTE SEMPRE!')
        break
