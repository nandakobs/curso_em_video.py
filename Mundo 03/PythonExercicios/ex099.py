from time import sleep


def maior(*num):
    print('Analisando os valores passados...')
    sleep(1)
    print(f'{num} foram os valores informados.\nSão {len(num)} números ao todo.')
    print(f'O maior valor informado foi {max(num)}.')
    print('=' * 30)
    sleep(1)

maior(1, 12, 123, 1234, 9, 8 , 7 ,6 ,4, 7 )
maior(2, 5, 6, 7, 1)
maior(1, 2)
maior(8)