valor = int(input('Digite um valor: '))
soma = valor
vezes = 1
maior = valor
menor = valor
res = ''
while res != 'N':
    res = str(input('Quer digitar outro valor? [S/N] ')).upper().strip()
    if res == 'S':
        valor = int(input('Digite outro valor: '))
        soma += valor
        vezes += 1
    if 'S' != res != 'N':
        print('Resposta Inválida! Tente novamente.')
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
media = soma / vezes
print('A média entre todos os valore é {:.2f}'.format(media))
print('O maior numero lido foi {} e o menor foi {}'.format(maior, menor))

"""
# Resolução da aula

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
"""