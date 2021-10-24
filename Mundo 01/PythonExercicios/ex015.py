kms = float(input('Quantos km o carro alugado percorreu? '))
dias = int(input('Por quantos dias ele foi alugado? '))
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 15 cent por km rodado
valor = (0.15 * kms) + (60 * dias)
print('O preço a ser pago é de R${:.2f}'.format(valor))

