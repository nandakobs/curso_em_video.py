tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('---FIM---')

# Versão Simplificada
print('carro novo' if tempo <= 3 else 'carro velho')
print('---FIM---')

nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nora: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
print('APROVADO' if m >= 6.0 else 'REPROVADO')


