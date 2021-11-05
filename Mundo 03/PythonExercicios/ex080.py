"""
num = []
for c in range(5):
    n = int(input('Insira um valor: '))
    num.append(n)
nums = num[:]
for pos, valor in enumerate(num):
    if valor == min(num):
        del num[pos]
        num.insert(0, valor)
    elif valor == max(num):
        num.append(valor)
        del num[pos]
    # 1, 2, 3
    elif valor > num[2] and valor > num[3]:
        del num[pos]
        num.insert(3, valor)
    elif valor > num[1] and valor > num[3]:
        del num[pos]
        num.insert(3, valor)
    elif valor > num[1] and valor > num[2]:
        del num[pos]
        num.insert(3, valor)
    elif valor > num[2] and valor > num[3]:
        del num[pos]
        num.insert(2, valor)
    elif valor > num[1] and valor > num[3]:
        del num[pos]
        num.insert(2, valor)
    elif valor > num[1] and valor > num[2]:
        del num[pos]
        num.insert(2, valor)
    elif valor > num[2] and valor > num[3]:
        del num[pos]
        num.insert(1, valor)
    elif valor > num[1] and valor > num[3]:
        del num[pos]
        num.insert(1, valor)
    elif valor > num[1] and valor > num[2]:
        del num[pos]
        num.insert(1, valor)
print(num)
nums.sort()
print(nums)"""

# Resolução da aula

lista = []
for c in range(0, 5):
    n = int(input('Digite uma valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionando ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionando na posição {pos} da lista..')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')