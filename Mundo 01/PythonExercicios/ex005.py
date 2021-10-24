n = int(input('Digite um numero inteiro: '))
antes= n - 1
depois= n + 1
print('O sucessor de {} é {}, e o antecessor é {}.'.format(n, antes, depois))
'''
Resolução da aula
Como não usaremos as variaveis antes e depois  pra qualquer coisa
podemos fazer o seguinte:
n = int(input('Digite um numero inteiro: '))
print('O sucessor de {} é {}, e o antecessor é {}.'.format(n, n-1, n+1))

'''