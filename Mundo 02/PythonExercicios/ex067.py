"""from time import sleep
while True:
    print('=' * 30)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('=' * 30)
    if n < 0:
        sleep(1)
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    c = 1
    while c < 11:
        print(f'{n} x {c:2} = {n*c}')
        c += 1

# Resolução da aula
# for c in range(1, 11):
#     print(f'{n} x {c:2} = {n * c}')"""


while True:
    print('=' * 30)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('=' * 30)
    if n < 0:
        break
    tabuada = [print(f'{n} x {c:2} = {n*c}') for c in range(10)]
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')