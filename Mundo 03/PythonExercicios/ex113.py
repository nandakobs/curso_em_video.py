def leiaint(valor=0):
    while True:
        try:
            valor = int(input('Digite um numero inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um numero inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar um numero inteiro\033[m')
            break
        else:
            break
    return valor


def leiafloat(valor=0):
    while True:
        try:
            valor = float(input('Digite um numero real: ').replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um numero real válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar um numero real\033[m')
            break
        else:
            break
    return valor



print('=' * 35)
print(f'Você digitou o número inteiro {leiaint()} e o número real {leiafloat()}')
