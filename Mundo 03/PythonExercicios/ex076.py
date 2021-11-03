listagem = ('Xerox B/P', 0.50, 'Xerox Colorida', 1.20, 'Scanear', 2, 'Fax', 3)
print('='*30)
print('{:^30}'.format('TIO ZÉ CÓPIAS'))
print('='*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<24}', end='')
    else:
        print(f'R${listagem[pos]:.>.2f}')
print('='*30)
print('{:^30}'.format('NÃO VENDEMOS FIADO'))
print('='*30)
