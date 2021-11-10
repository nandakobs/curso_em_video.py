from utilidadesCeV import moeda
p = float(input('Digite o preço: R$').replace(',', '.'))
moeda.resumo(p, 80, 35)