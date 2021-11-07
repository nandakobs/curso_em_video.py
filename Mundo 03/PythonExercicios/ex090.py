alune = dict()
alune['Nome'] = str(input('Nome: ')).strip()
alune['Média'] = float(input(f'Média de {alune["Nome"]}: '))
if alune['Média'] >=7:
    alune['Situação'] = '\033[32mAprovado\033[m'
elif 5 <= alune['Média'] < 7:
    alune['Situação'] = '\033[33mRecuperação\033[m'
else:
    alune['Situação'] = '\033[31mReprovado\033[m'
print('='*30)
for a, b in alune.items():
    print(f'{a} é igual a {b}')