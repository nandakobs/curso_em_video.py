ano = int(input('Digite um ano pra verificar se ele é bissexto: '))
bi = ano / 4
if bi.is_integer():
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))

"""
# Resolução da aula

from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual. '))
if ano == 0:
    ano = date.today().year #pega a data de hoje, em especifico o ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
"""
