
# ALTERNATIVA 1
def area():
    larg = float(input('LARGURA (m): '))
    comp = float(input('COMPRIMENTO (m): '))
    ar = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {ar}m²')


print(' Controle de Terrenos')
print('='*22)
area()


# ALTERNATIVA 2

def area(larg, comp):
    ar = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {ar}m²')


print(' Controle de Terrenos')
print('='*22)
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))

# 4.5 x 8 = 36m²


# RESOLUÇÃO DA AULA

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')


print(' Controle de Terrenos')
print('='*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)