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
print(f'[ {lista[0][0]} ][ {lista[0][1]} ][ {lista[0][2]} ]\n'
      f'[ {lista[1][0]} ][ {lista[1][1]} ][ {lista[1][2]} ]\n'
      f'[ {lista[2][0]} ][ {lista[2][1]} ][ {lista[2][2]} ]\n')

# Resolução da aula

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()