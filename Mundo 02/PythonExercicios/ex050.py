soma = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma = soma + n
print(soma)

# Resolução da aula

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))
