from time import sleep
print('\033[1;36m='*22)
print('= Calculadora de IMC =')
print('='*22)
peso = float(input('Peso: ').replace(',', '.'))
altura = float(input('Altura: ').replace(',', '.'))
imc = peso / (altura * altura) # ou altura ** 2
print('\nCalculando seu IMC...\n')
sleep(1)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc >= 18.5 and imc <= 25:
    print('Você tem o peso ideal.')
elif imc >= 25 and imc <= 29.9:
    print('Você está acima do peso ideal.')
elif imc >= 30 and imc <= 40:
    print('Você está obeso(a).')
elif imc > 40:
    print('Você está com obesidade mórbida.')
