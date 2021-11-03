brasileirao = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Bragantino', 'Fortaleza', 'Corinthians', 'Internacional',
               'Fluminense', 'América-MG', 'Cuiabá', 'Atlético-GO', 'São Paulo', 'Ceará SC', 'Athletico-PR', 'Santos',
               'Bahia', 'Sport Recife', 'Juventude', 'Grêmio', 'Chapecoense')
print(f'Lista de times do brasileirão: {brasileirao}')
print('='*50)
print(f'Os 5 primeiros são: {brasileirao[:5]}')
print('='*50)
print(f'Os 4 últimos são: {brasileirao[-4:]}')
print('='*50)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('='*50)
print(f'O Chapecoense está na {brasileirao.index("Chapecoense") + 1}ª posição')
