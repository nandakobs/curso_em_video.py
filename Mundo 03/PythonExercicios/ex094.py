people = list()
pessoa = dict()
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
    while 'M' != pessoa['sexo'] != 'F':
        print('ERRO! Por favor, digite apenas M ou F')
        pessoa['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    people.append(pessoa.copy())
    pessoa.clear()
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while 'S' != continua != 'N':
        print('ERRO! Responda apenas S ou N.')
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('=' * 50)
print(f'— O grupo tem {len(people)} pessoas.')
soma = media = 0
muie = list()
for v in people:
    soma += v['idade']
    if v['sexo'] == 'F':
        muie.append(v['nome'])
media = soma / len(people)
print(f'— A média de idade é de {media:.2f} anos.\n'
      f'— As mulheres cadastradas foram: {", ".join(muie)}\n'
      f'— Lista das pessoas que estão acima da média:\n')
for v in people:
    if v['idade'] > media:
        print(f'nome = {v["nome"]}; sexo = {v["sexo"]}; idade = {v["idade"]}')
print('\n<< ENCERRADO >>')

"""
# Resolução da aula
while True:
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    if pessoa['sexo'] in 'MF':
        break
    print('ERRO! Por favor, digite apenas M ou F')
"""