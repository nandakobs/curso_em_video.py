"""
n = int(input('Diga ai um número: '))
lista = [n, n, ]
atual = 1
ant = 0
seq = 2
while len(lista) != n:
    conta = lista[atual] + lista[ant]
    lista.append(conta)
    atual += 1
    ant += 1
    seq += 1
print('A sequencia de Fibonacci é {}'.format(lista))
"""

# Resolução da aula

print('='*30)
print('Sequência de Fibonacci')
print('='*30)
n = int(input('Quantos termos você quer mostrar? '))
print('='*30)
t1 = 0
t2 = 1
cont = 3
print('{} -> {}'.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('='*30)
