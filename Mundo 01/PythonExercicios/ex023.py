# Manipulando strings - ex023
# Faça um programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos digitos separados.
# Ex: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

"""
TENTATIVA 01
num = input('Digite um numero: ')
unidade = num[len(num) - 1]
dezena = num[len(num) - 2]
centena = num[len(num) - 3]
milhar = num[len(num) - 4]
print(len(num))  # pra saber se a contagem está certa
if len(num) == 1:
    print('unidade: {}'.format(unidade))
    # Quando apenas 1 num é digitado, da o seguinte erro:
    # centena = num[len(num)-3]
    # IndexError: string index out of range
    # PORQUE??
elif len(num) == 2:
    print('unidade: {}'.format(unidade))
    print('dezena: {}'.format(dezena))
elif len(num) == 3:
    print('unidade: {}'.format(unidade))
    print('dezena: {}'.format(dezena))
    print('centena: {}'.format(centena))
elif len(num) == 4:
    print('unidade: {}'.format(unidade))
    print('dezena: {}'.format(dezena))
    print('centena: {}'.format(centena))
    print('milhar: {}'.format(milhar))
"""
"""
TENTATIVA 02
# não da certo pq ele da erro se n dor 4 numeros
num = input('Digite um número: ')
unidade = num[0]
dezena = num[1]
centena = num[2]
milhar = num[3]
print('unidade: {}'.format(unidade))
print('dezena: {}'.format(dezena))
print('centena: {}'.format(centena))
print('milhar: {}'.format(milhar))
"""
"""
TENTATIVA 03
# da erro com menos de 4 numeros
num = input('Digite um numero: ')
unidade = num[0]
dezena = num[1]
centena = num[2]
milhar = num[3]
print('unidade: {}'.format(num[0]))
print('dezena: {}'.format(num[1]))
print('centena: {}'.format(num[2]))
print('milhar: {}'.format(num[3]))"""



#TENTATIVA QUE DEU CERTOOOO

num = input('Digite um numero: ')
print('Temos', (len(num)), 'número(s).')  # pra saber se a contagem está certa
if len(num) == 1:
    print('unidade: {}'.format(num[0]))
elif len(num) == 2:
    print('unidade: {}'.format(num[0]))
    print('dezena: {}'.format(num[1]))
elif len(num) == 3:
    print('unidade: {}'.format(num[0]))
    print('dezena: {}'.format(num[1]))
    print('centena: {}'.format(num[2]))
elif len(num) == 4:
    print('unidade: {}'.format(num[0]))
    print('dezena: {}'.format(num[1]))
    print('centena: {}'.format(num[2]))
    print('milhar: {}'.format(num[3]))
else:
    print('Número inválido. Digite um número entre 0 e 9999.')



"""
# Resolução da aula: tratando como int

num = int(input('Informe um número: '))
u = num // 1 % 10  # divide o numero por 1, dps divido por 10 e pego o resto da divisão q é a unidade
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número{}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))"""


