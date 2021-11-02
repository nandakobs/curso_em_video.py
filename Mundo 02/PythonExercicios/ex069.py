homis = maiores = muie = 0
while True:
    print('=' * 30)
    print('CADASTRE UMA PESSOA')
    print('=' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while 'M' != sexo != 'F':
        print('Resposta Inválida.')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homis += 1
    if idade > 18:
        maiores += 1
    if sexo == 'F' and idade < 20:
        muie += 1
    print('=' * 30)
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while 'N' != continua != 'S':
        print('Resposta Inválida.')
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('===== FIM DO CADASTR0 =====')
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homis} homens cadastrados')
print(f'E temos {muie} mulheres com menos de 20 anos')

"""
# Resolução da aula
sexo = ' '
while sexo not in 'MF':
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
"""



