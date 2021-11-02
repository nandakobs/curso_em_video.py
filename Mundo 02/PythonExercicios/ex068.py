from random import randint
print('-=' * 15)
print('== VAMOS JOGAR PAR OU ÍMPAR ==')
print('-=' * 15)
cont = 0
while True:
    pc = randint(0, 100)
    n = int(input('Diga um valor: '))
    pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper().replace('Í', 'I')[0]
    print('-=' * 15)
    s = n + pc
    par = True if s % 2 == 0 else False
    if par:
        print(f'Você jogou {n} e o computador {pc}. {s} é PAR')
        print('-=' * 15)
    else:
        print(f'Você jogou {n} e o computador {pc}. {s} é ÍMPAR')
        print('-=' * 15)
    if pi == 'P':
        if par:
            cont += 1
            print('Você VENCEU!\nVamos jogar novamente...')
            print('=' * 30)
        else:
            print('Você PERDEU!')
            break
    elif pi == 'I':
        if not par:
            cont += 1
            print('Você VENCEU!\nVamos jogar novamente...')
            print('=' * 30)
        else:
            print('Você PERDEU!')
            break
    else:
        print('Resposta Inválida. Informe se é par ou ímpar.\nTente novamente.')
print('-=' * 15)
print(f'\033[1;31mGAME OVER!\033[m Você venceu {cont} vezes.')
print('-=' * 15)
