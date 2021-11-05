nums = []
par = []
impar = []
while True:
    n = int(input('Insira um valor: '))
    nums.append(n)
    continua = ' '
    while 'S' != continua != 'N':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
for valor in nums:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print('='*50)
print(f'A lista completa é {nums}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')