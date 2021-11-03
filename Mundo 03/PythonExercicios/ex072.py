extensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while 0 < n > 20:
        print('\033[31mResposta Inválida. Tente novamente.\033[m')
        n = int(input('Digite um número entre 0 e 20: '))
    print('=' * 30)
    print(f'Você digitou o número {extensos[n]}.')
    print('=' * 30)
    continua = ''
    while 'N' != continua != 'S':
        continua = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break




"""
# Resolução da aula
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end='')"""