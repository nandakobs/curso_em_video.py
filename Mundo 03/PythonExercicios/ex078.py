"""nums = []
for cont in range(5):
    cont = int(input(f'Insira um valor para a Posição {cont}: '))
    nums.append(cont)
print('=' * 50)
print(f'Você digitou os valores {nums}')
maior_v = menor_v = maior_p = menor_p = 0
listame = []
listama = []
for pos, c in enumerate(nums):
    if pos == 0:
        maior_p = menor_p = pos
        maior_v = menor_v = c
    elif c == maior_v:
        listama.append(maior_p)
        listama.append(pos)
    elif c == menor_v:
        listame.append(menor_p)
        listame.append(pos)
    if c > maior_v:
        maior_v = c
        maior_p = pos
    if c < menor_v:
        menor_p = pos
        menor_v = c
if len(listama) == 0:
    print(f'O maior número digitado é {maior_v} e está na posição {maior_p} da lista.')
else:
    print(f'O maior número digitado é {maior_v} e está nas posições {listama} da lista.')
if len(listame) == 0:
    print(f'O menor número digitado é {menor_v} e está na posição {menor_p} da lista.')
else:
    print(f'O menor número digitado é {menor_v} e está nas posições {listame} da lista.')
"""
# Resolução da aula

listanum = []
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Insira um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('-=' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print() # print vazio que quebra o end
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end='')
print()
