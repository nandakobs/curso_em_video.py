print('Vamos calcular seu aumento!')
salario = float(input('Qual é seu salário atual? R$').replace(',', '.'))
if salario <= 1250.00:
    aumento = salario * (15/100)
    salario = salario + aumento
    print('Você recebeu aumento de 15% e seu novo salario é: {:.2f}'.format(salario))
else:
    aumento = salario * (10/100)
    salario = salario + aumento
    print('Você recebeu aumento de 10% e seu novo salario é: {:.2f}'.format(salario))

# Resolução da aula

