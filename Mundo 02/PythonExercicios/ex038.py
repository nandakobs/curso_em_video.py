print('\033[1;33m='*30)
print('\033[1;32m  Comparador de numeros')
print('\033[1;33m=\033[m'*30)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
