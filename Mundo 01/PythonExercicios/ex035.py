"""print('Insira o valor de 3 retas para verificar se podem formar um trinagulo')
reta1 = int(input('Reta 1: '))
reta2 = int(input('Reta 2: '))
reta3 = int(input('Reta 3: '))
soma = reta1 + reta2
if soma > reta3:
    print('Pode formar triangulo')
else:
    print('Não pode formar triangulo')"""

#Resolução da aula

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')
