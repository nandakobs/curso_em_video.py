peso = []
for c in range(1, 6):
    add = float(input('Digite seu peso em KG: ').replace(',', '.'))
    peso.append(add)
#print(peso)
print('O maior peso lido foi {}'.format(max(peso)))
print('O menor peso lido foi {}'.format(min(peso)))

# Resolução da aula
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}KG'.format(maior))
print('O menor peso lido foi de {}KG'.format(menor))

