from time import sleep
print('\033[1;33m='*40)
print('\033[1;32m  Bem-vindo a Simulação de Empréstimo!')
print('\033[1;33m='*40)
valor_casa = float(input('\033[1;32mQual é o valor da casa? '))
salario = float(input('Qual é o seu salario atual? '))
anos = int(input('Em quantos anos você pretende pagar? '))
prestaçao = valor_casa / (anos * 12)
print('\033[1;33m='*40)
print('\033[1;32m      Analisando as condições...')
print('\033[1;33m='*40)
sleep(2)
if prestaçao <= salario * (30/100):
    print('\033[1;32mVocê pagará R${:.2f} mensais durante {} anos.'.format(prestaçao, anos))
else:
    print('\033[1;31mInfelizmente, você não pode financiar essa casa.'
          '\nO valor das parcelas ultrapassa 30% do seu salário.')