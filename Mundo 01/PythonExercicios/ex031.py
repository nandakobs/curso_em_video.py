distancia = float(input('Qual é a distancia da viagem em km? '))
if distancia <= 200.0:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
# Forma simplificada
# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagem é de R${:.2f}'.format(preço))