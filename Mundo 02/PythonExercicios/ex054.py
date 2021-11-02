from datetime import date
menores = 0
maiores = 0
for c in range(1, 8):
    ano = int(input('Digite ano de nascimento: '))
    idade = date.today().year - ano
    if idade < 21:
        menores += 1
    else:
        maiores += 1
print('Dessas 7 pessoas {} são menores de idade e {} são maiores de idade.'.format(menores, maiores))

#nasc = int(input('Em que ano a {}° pessoa nasceu?'.format(pess)))
