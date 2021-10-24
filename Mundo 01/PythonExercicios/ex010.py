real = float(input('Quanto você tem na carteira? R$'))
#considere US$1.00 = R$3.27 (o sonho kk)
#atualizando pros dias de hj 23/10/21
# valor / dolar ou dolar * valor
convertUS = real / 5.65
convertEUR = real / 6.58
convertIEN = real / 0.050
print("Com R${} você pode comprar:\n{:.2f} doláres\n{:.2f} euros\n{:.2f} ienes".format(real, convertUS, convertEUR, convertIEN))


