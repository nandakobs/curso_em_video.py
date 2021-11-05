"""
Diferentemente de tuplas, listas são mutáveis e são identificadas pelos colchetes.

Existem duas formas de criar uma lista
teste = []  OU  teste = list()
"""

lanche = ['burguer', 'suco', 'pizza', 'pudim']
print(lanche)
lanche[3] = 'picole'
print(lanche)  # ['burguer', 'suco', 'pizza', 'picole']
lanche.append('cookie') # adicionando no final
print(lanche)  # ['burguer', 'suco', 'pizza', 'picole', cookie]
lanche.insert(0, 'hot dog')  # adicionando na posição zero
print(lanche)  # ['hot dog', 'burguer', 'suco', 'pizza', 'picole', 'cookie']

# Formas de eliminar elementos da lista:
del lanche[3]
lanche.pop(3) #geralmente elimina o ultimo elemento mais vc pode indicar qual vc quer eliminar
lanche.remove('cookie')
# Todos eles eliminam o elemento e reorganizam a lista

if 'pizza' in lanche:
    lanche.remove('pizza')
#Verifica se está na lista e se sim, remove

valores = list(range(4, 11)) #cria uma lista com n°s de 4 a 10
print(valores)

nums = [8, 2, 5, 4, 9, 3, 0]
#nums.sort()  # organiza por ordem crescente ou alfabetica
print(nums)
#nums.sort(reverse=True) # organiza em ordem decrescente
print(nums)
len(nums)  # Retorna quantos elementos tem em num, são 7 (0, e de 1 a 6)

nums.append(2)  # Adicionei o n° 2 lá no final
print(nums)
nums.remove(2)  # Remove a primeira aparição de 2
print(nums)

print('='*50)

valorr = []
valorr.append(5)
valorr.append(9)
valorr.append(4)
print(valorr)

for v in valorr:  # para cada valor/elemento em valorr
    print(f'{v}...', end='')
print('=')
for c, v in enumerate(valorr): #enumerate ele pega tanto a posição quanto o valor dos elementos
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')


ota = []
for cont in range(0, 5):  # Adicionei 5 elementos a minha lista ota por meio de input
    ota.append(int(input('Digite um valor: ')))
print(ota)
print('='*20)

a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('='*20)
# Perceba que a partir do momento que eu
# igualo uma lista com a outra, o Python
# faz uma ligação entre elas.
# Pra resolver isso podemos criar uma cópia
b = a[:]
b[0] = 47
print(f'Lista A: {a}')
print(f'Lista B: {b}')



