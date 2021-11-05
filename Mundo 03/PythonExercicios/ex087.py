lista =[[], [], []]
for c in range(3):
    zero = int(input(f'Digite um valor para [0,{c}]: '))
    lista[0].append(zero)
for c in range(3):
    um = int(input(f'Digite um valor para [1,{c}]: '))
    lista[1].append(um)
for c in range(3):
    dois = int(input(f'Digite um valor para [2,{c}]: '))
    lista[2].append(dois)
print('='*30)
print(f'[ {lista[0][0]:^5} ][ {lista[0][1]:^5} ][ {lista[0][2]:^5} ]\n'
      f'[ {lista[1][0]:^5} ][ {lista[1][1]:^5} ][ {lista[1][2]:^5} ]\n'
      f'[ {lista[2][0]:^5} ][ {lista[2][1]:^5} ][ {lista[2][2]:^5} ]\n')
soma = 0
for e in range(3):
    for c in lista[e]:
        if c % 2 == 0:
            soma += c
print(f'A soma de todos os valores pares digitados é: {soma}')
soma2 = lista[0][2] + lista[1][2] + lista[2][2]
print(f'A soma dos valores da terceira coluna é {soma2}')
print(f'O maior valor da segunda linha é {max(lista[1])}')

# Resolução da aula

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')