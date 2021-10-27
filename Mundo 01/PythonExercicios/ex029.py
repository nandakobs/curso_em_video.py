speed = float(input('Velocidade do carro em km/h: '))
if speed > 80.0:
    print('Você foi multado!')
    multa = 7.0 * (speed - 80.0)
    print('A multa de R${:.2f} foi enviada por email.'.format(multa))
else:
    print('Tu tá na lei! Siga de boas.')