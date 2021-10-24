preco = float(input('Insira preço do produto: R$'))
desconto = preco * 0.05
novo_preco = preco - desconto
print('O novo preço com desconto de 5% é {:.2f}'.format(novo_preco))
#dica n * porcentagem / 100  >>> 120 * 10/100 >> 10% de 120
# novo_preço = preço - (preço * 10/100)