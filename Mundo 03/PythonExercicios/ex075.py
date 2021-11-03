lista = []
par = []
for c in range(1, 5):
    c = int(input(f'Insira o {c}° valor:'))
    lista.append(c)
    if c % 2 == 0:
        par.append(c)
tupla = (lista[0], lista[1], lista[2], lista[3])
print('=' * 30)
print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição.' if 3 in tupla else f'O valor 3 não foi digitado em nenhuma posição.')
print(f'Não foram digitados valores pares.' if not par else f'Não foram digitados valores pares.')

"""
# Resolução da aula
num =(int(input('Digite um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite o ultimo número: ')))
"""