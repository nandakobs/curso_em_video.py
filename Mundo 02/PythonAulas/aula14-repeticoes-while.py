"""
Quando você sabe o limite é muito mais prático o usar o for
Quando você não sabe o limite use o while

while not apple:
    passo
pega

while not apple:
    if chão a frente:
        passo
    if buraco a frente:
        pula
    if moeda:
        pega
pega
"""
"""
for c in range(1, 10):
    print(c)
print('FIM do for')

a = 1
while a < 10:
    print(a)
    a += 1
print('FIM do while')
"""
"""
n = 1
nums = []
while n != 0:
    n = int(input('DIGITE UM VALOR: '))
    nums.append(n)
print('FIM')
print(nums)

r = 'S'
while r == 'S':
    n = int(input("Digite um valor: "))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')
"""

num = 1
par = 0
impar = 0
while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares.'.format(par, impar))
