"""
while True:
    if chão a frente:
        passo
    if buraco a frente:
        pula
    if moeda:
        pega
    if troféu:
        pula
        break
pega
"""
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale %s' % (s))   # Python 2
print('A soma vale {}'.format(s))  # Python 3
print(f'A soma vale {s}')   # Python 3.6 em diante

nome = 'Maria'
idade = 22
salario = 987.3
print(f'A {nome:-^20} tem {idade} anos e ganha R${salario:.2f}')
# ^ centraliza em tantos espaços
# > alinha a direita
# < alinha a esquerda