m = float(input('Valor em metros: '))
km = m / 1000
cm = m * 100
ml = m * 1000
hec = m / 100
deca = m / 10
deci = m * 10
print('{} metro(s) são:\n{:.0f} centimetros\n{:.0f} milimetros\n'
      '{:.3f} quilometros\n{:.3f} hectometros\n{:.3f} decametro\n'
      '{:.0f} decimetros'.format(m, cm, ml, km, hec, deca, deci))
