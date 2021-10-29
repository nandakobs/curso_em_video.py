"""
num = int(input('Numero a ser convertido: '))
print('Escolha a base de conversão: ')
base = int(input('[1]Binário  [2]Octal  [3]Hexadecimal \n'))
if base == 1:

elif base == 2:

elif base == 3:

else:
    print('Base escolhida não existente!')

"""

# Resolução da aula
num = int(input('Digite um numero inteiro: '))
print("""Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXDECIMAL""")
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')