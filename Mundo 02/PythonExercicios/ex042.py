print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo', end='')
    if r1 == r2 == r3:  # se r2 é = a r1, e se r2 é igual a r3
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:  # se r2!=r1 e r2=!r3 e r3!=r1
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')
