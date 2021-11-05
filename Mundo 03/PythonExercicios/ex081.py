valores = []
while True:
    n = int(input('Insira um valor: '))
    valores.append(n)
    continua = ' '
    while 'S' != continua != 'N':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
valores.sort(reverse=True)
print('='*50)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
print(f'O valor 5 está na lista' if 5 in valores else f'O valor 5 não aparece na lista')

"""
# Resolução da aula
  
  valores.append(int(input('Digite um numero: ')))
  resp = str(input('Quer continuar [S/N] '))
  if resp in 'Nn':
      break
"""