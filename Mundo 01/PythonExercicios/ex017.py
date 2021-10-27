from math import hypot
cat_op = float(input('Comprimento do cateto oposto: '))
cat_adj = float(input('Comprimento do cateto adjacente: '))
hipo = hypot(cat_op, cat_adj)
print('O comprimento da hipotenusa é: {:.2f}'.format(hipo))

"""
Resoluções da aula:

cat_op = float(input('Comprimento do cateto oposto: '))
cat_adj = float(input('Comprimento do cateto adjacente: '))
hipo = (cat_op ** 2 + cat_adj ** 2) ** (1/2)
print('O comprimento da hipotenusa é: {:.2f}'.format(hipo))

"""