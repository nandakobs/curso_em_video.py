for c in range(1, 51):
    par = c % 2
    print('.', end='')
    # sem necessidade da variavel, operação poderia ser realizada direto no if
    if par == 0:
        #print(c)
        print(c, end=' ') #pros numeros ficarem lado a lado
print('Esses são os números pares de 1 a 50')

# Perceba os 2 pontos em antes de cada numero, ou seja
# ele faz algumas repetições sem mostrar valor, então poderiamos
# fazer de uma maneira melhor

#Resolução da aula

for n in range(2, 51, 2):
    print('.', end=' ')
    print(n, end=' ')
print('ACABOU')

"""
Perceba que agr só aparecem 1 pontinho
ele fez metade do trabalho
e ocupou do seu processador metade do tempo
"""
