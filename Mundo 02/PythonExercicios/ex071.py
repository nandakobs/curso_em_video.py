"""
from math import floor
print('=' * 30)
print('BANCO CEV')
print('=' * 30)
valor = int(input('Qual valor você quer sacar? R$'))
sobrou = c50 = c20 = c10 = c1 = 0
if valor >= 50:
    c50 = valor / 50
    sobrou = valor % 50
    c50 = floor(c50)
    print(f'Total de {c50:.0f} cédulas de R$50')
    if sobrou <= 20:
        c20 = sobrou / 20
        sobrou = valor % 20
        c20 = floor(c20)
        if c20 >= 1:
            print(f'Total de {c20:.0f} cédulas de R$20')
    if sobrou >= 19 and sobrou <= 10:
        c10 = sobrou / 10
        sobrou = valor % 10
        c10 = floor(c10)
        if c10 >= 1:
            print(f'Total de {c10:.0f} cédulas de R$10')
    if sobrou <= 9 and sobrou >= 5:
        c5 = sobrou / 5
        sobrou = valor % 5
        c5 = floor(c5)
        if c5 >= 1:
            print(f'Total de {c5:.0f} cédulas de R$5')
    if sobrou <= 4:
        c1 = sobrou / 1
        sobrou = valor % 1
        c1 = floor(c1)
        if c1 >= 1:
            print(f'Total de {c1:.0f} cédulas de R$1')
elif valor <= 49:
    c20 = valor / 20
    sobrou = valor % 20
    c20 = floor(c20)
    print(f'Total de {c20:.0f} cédulas de R$20')
    if sobrou <= 19 and sobrou >= 10:
        c10 = sobrou / 10
        sobrou = valor % 10
        c10 = floor(c10)
        if c10 >= 1:
            print(f'Total de {c10:.0f} cédulas de R$10')
    if sobrou <= 9 and sobrou >= 5:
        c5 = sobrou / 5
        sobrou = valor % 5
        c5 = floor(c5)
        if c5 >= 1:
            print(f'Total de {c5:.0f} cédulas de R$5')
    if sobrou <= 4:
        c1 = sobrou / 1
        sobrou = valor % 1
        c1 = floor(c1)
        if c1 >= 1:
            print(f'Total de {c1:.0f} cédulas de R$1')
elif valor <= 19:
    c10 = valor / 10
    sobrou = valor % 10
    c10 = floor(c10)
    print(f'Total de {c10:.0f} cédulas de R$10')
    if sobrou <= 9 and sobrou >= 5:
        c5 = sobrou / 5
        sobrou = valor % 5
        c5 = floor(c5)
        if c5 >= 1:
            print(f'Total de {c5:.0f} cédulas de R$5')
    if sobrou <= 4:
        c1 = sobrou / 1
        sobrou = valor % 1
        c1 = floor(c1)
        if c1 >= 1:
            print(f'Total de {c1:.0f} cédulas de R$1')
elif valor <= 9:
    c5 = valor / 5
    sobrou = valor % 5
    c5 = floor(c5)
    if c5 >= 1:
        print(f'Total de {c5:.0f} cédulas de R$5')
    if sobrou <= 4:
        c1 = sobrou / 1
        sobrou = valor % 1
        c1 = floor(c1)
        if c1 >= 1:
            print(f'Total de {c1:.0f} cédulas de R$1')
elif valor <= 4:
    c1 = valor / 1
    sobrou = valor % 1
    c1 = floor(c1)
    print(f'Total de {c1:.0f} cédulas de R$1')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
# 50, 20, 10, 1
"""

# Resolução da aula

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')