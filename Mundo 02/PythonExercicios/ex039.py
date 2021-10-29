import sys
from datetime import datetime
from time import sleep
from sys import exit

print('\033[1;32m='*40)
print('\033[1;32m Checagem para Alistamento do Exercito')
print('\033[1;32m=\033[m'*40)

sexo = str(input('Qual é seu sexo biológico?')).upper().strip()
if sexo == 'FEMININO':
    print('O alistamento para mulheres não é obrigatório.')
    continua = str(input('Deseja continuar? [S/N]')).upper().strip()
    if continua == 'N':
        print('Obrigada por usar o programa.')
        exit()
    elif continua != 'N' and continua != 'S':
        print('Resposta inválida! Tente novamente.')
elif sexo != 'FEMININO' and sexo != 'MASCULINO':
    print('Resposta inválida! Tente novamente.')

ano = int(input('Qual é o seu ano de nascimento? '))
print('\n\033[1;32mAnalisando... \033[m\n')
sleep(2)
ano = datetime.now().year - ano
if ano < 18:
    falta = 18 - ano
    print('Você terá que se alistar em {} ano(s).'.format(falta))
elif ano == 18:
    print('Chegou a hora de se alistar!')
else:
    passou = ano - 18
    print('Você deveria ter se alistado a {} anos.'.format(passou))

"""
# Resolução da aula

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
"""