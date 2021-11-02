"""print('===== ARITHMETIC PROGRESSION CALCULATOR =====')
termo1 = int(input('Insira o 1° termo: '))
razao = int(input('Insira a razão: '))

#TENTATIVA 01 : ERRO
pa = []
for c in range(1, 10):
    pa[c] = pa[(c-1)] + razao
print(pa)

#TENTATIVA 02 : OK
lista = termo1 + (10 - 1) * razao
lista = lista + 1
for c in range(termo1, lista, razao):
    print(c)"""

# Resolução da aula

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão # definindo o decimo termo, onde para de contar
for c in range(primeiro, decimo + razão, razão):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
