salario = float(input('Qual é o salario atual?'))
aumento = salario * 0.15 # ou salario * 15/100
novo_salario = salario + aumento
print('O novo salario com 15% de aumento é R${:.2f}'.format(novo_salario))