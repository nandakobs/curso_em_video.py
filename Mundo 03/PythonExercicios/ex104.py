"""
# TENTATIVA 1
def leiaint():
    while True:
        try:
            num = int(input('Digite um numero: '))
        except ValueError:
            print('\033[31mERRO! Por favor, digite um numero\033[m')
        else:
            print('=' * 35)
            print(f'Você acabou de digitar o numero {num}')
            break


leiaint()
"""


def leiaint(valor):
    while True:
        try:
            a = int(input(valor))
        except ValueError:
            print('\033[31mERRO! Por favor, digite um numero\033[m')
        else:
            print('=' * 35)
            break
    return a


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')

"""
# Resolução da aula
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Por favor, digite um numero inteiro válido\033[m')
        if ok:
            break
    return valor

n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
"""