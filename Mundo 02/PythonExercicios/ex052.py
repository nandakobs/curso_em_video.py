n = int(input('Digite um numero inteiro: '))
multiplo = 0
for c in range(2, n):
    if n % c == 0:
        #print('Multiplo de {}'.format(c))
        multiplo += 1
if multiplo == 0:
    print('É PRIMO')
else:
    print('NÃO É PRIMO\npois é multiplo de {} numero(s) além dele mesmo e 1.'.format(multiplo))

# Resolução da aula

num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')