from time import sleep
from datetime import datetime
print('\033[1;34m='*36)
print('= CONFEDERAÇÃO NACIONAL DE NATAÇÃO =')
print('='*36)
print('====== AVALIAÇÂO DE CATEGORIA ======')
ano = int(input('\nQual é o ano de nascimento do atleta? '))
ano = datetime.now().year - ano
sleep(1)
print('\nAtleta tem {} anos.'.format(ano))
if ano <= 9:
    print('CATEGORIA: MIRIM')
elif ano <= 14:
    print('CATEGORIA: INFANTIL')
elif ano <= 19:
    print('CATEGORIA: JUNIOR')
elif ano <=25:
    print('CATEGORIA: SÊNIOR')
else:
    print('CATEGORIA: MASTER')
