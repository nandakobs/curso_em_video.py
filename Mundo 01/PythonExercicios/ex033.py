n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('E mais um: '))

numeros = [n1, n2, n3]
print(numeros)

if n1 > n2 and n1 > n3:
    print('{} é o maior numero'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} é o maior numero'.format(n2))
else:
    print('{} é o maior numero.'.format(n3))

if n1 < n2 and n1 < n3:
    print('{} é o menor numero'.format(n1))
elif n2 < n1 and n2 < n3:
    print('{} é o menor numero'.format(n2))
else:
    print('{} é o menor numero.'.format(n3))

"""
# Resolução da aula

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
"""