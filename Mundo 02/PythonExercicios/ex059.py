from time import sleep
print('-='*12)
print('CALCULADORA DE 2 VALORES')
print('-='*12)
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
op = 0
while op != 5:
    print('Selecione a operação a ser realizada:\n'
                   '[1]Somar [2]Multiplicar [3]Maior '
                   '[4]Novos Números [5]SAIR')
    op = int(input('Operação selecionada: '))
    if op == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            maior = n1
            menor = n2
            print('{} é maior que {}'.format(maior, menor))
        elif n1 == n2:
            print('Os números tem valor igual.')
        else:
            maior = n2
            menor = n1
            print('{} é maior que {}'.format(maior, menor))
    elif op == 4:
        n1 = int(input('Digite o 1° valor: '))
        n2 = int(input('Digite o 2° valor: '))
    elif op != 5:
        print('Operação não reconhecida. Tente novamente.')
    print('=' * 30)
print('Finalizando...')
sleep(1)
print('\n===== CALCULADORA ENCERRADA =====')