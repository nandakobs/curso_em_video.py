n = int(input('Gerar a tabuada de: '))
for c in range(1, 11):
    tabuada = n * c
    print('{} x {:2} = {}'.format(n, c, tabuada))

#Resolução da aula

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'. format(num, c, num * c))