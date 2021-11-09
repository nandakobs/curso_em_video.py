from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {str(passo).replace("-", "")} em {str(passo).replace("-", "")}')
    if inicio > fim and passo > 0:
        passo = -abs(passo)
    finzin = fim + passo
    for c in range(inicio, finzin, passo):
        print(c, end=', ')
        sleep(1)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
