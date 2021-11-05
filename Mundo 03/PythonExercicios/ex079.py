valores = []
while True:
    n = int(input('Insira um valor: '))
    if n in valores:
        print('Valor duplicado! Não será adicionado.')
    else:
        print('Valor adicionado com sucesso!')
        valores.append(n)
    continua = ' '
    while 'S' != continua != 'N':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
valores.sort()
print('='*50)
print(f'Você digitou os valores {valores}')