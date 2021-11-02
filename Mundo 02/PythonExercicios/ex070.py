print('=' * 30)
print('{:-^30}'.format(' LOJAS SUPER BARATÃO '))
print('=' * 30)
total = caros = 0
menor = 100000000000
nome_barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$').replace(',', '.'))
    total += preco
    if preco > 1000:
        caros += 1
    if preco < menor:
        nome_barato = nome
        menor = preco
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while 'N' != continua != 'S':
        print('Resposta Inválida.')
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('====== COMPRA FINALIZADA ======')
print(f'Total da compra: R${total:.2f}')
print(f'Temos {caros} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_barato} que custa R${menor:.2f}')

"""
# Resolução da aula
cont = menor = 0
if cont == 1 or preço < menor:
        menor = preço
        barato = produto
resp = ' '
while resp not in 'SN':
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
"""
