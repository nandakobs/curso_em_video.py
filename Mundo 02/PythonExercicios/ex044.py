print('\033[1;36m='*22)
print('= CAIXA SUPERMERCADO =')
print('='*22)
preco = float(input('\nTOTAL A PAGAR: R$ '))
pag = float(input('SELECIONE O MÉTODO DE PAGAMENTO:'
                  '\n [1]DINHEIRO/CHEQUE [2]CARTÃO\n'))
if pag == 1:
    a_vista = preco - (preco * (10/100))
    print('CUPOM 10% DE DESCONTO APLICADO'
          '\nTOTAL A PAGAR: R${:.2f}'.format(a_vista))
elif pag == 2:
    metodo = float(input('MÉTODO CARTÃO SELECIONADO'
                         '\n[1]À VISTA [2]PARCELADO 2X [3]PARCELADO 3X OU MAIS\n'))
    if metodo == 1:
        a_vista = preco - (preco * (5 / 100))
        print('CUPOM 5% DE DESCONTO APLICADO'
              '\nTOTAL A PAGAR: R${:.2f}'.format(a_vista))
    elif metodo == 2:
        parcelas = preco / 2
        print('2X DE {:.2f} S/JUROS'.format(parcelas),
              '\nTOTAL: R${:.2f}'.format(preco))
    elif metodo == 3:
        parcelas = int(input('EM QUANTAS VEZES? '))
        com_juros = preco + (preco * (20/100))
        divisao = com_juros / parcelas
        print('{}X DE {:.2f} C/JUROS NO VALOR DE R${:.2f}'.format(parcelas, divisao, preco * (20/100)),
              '\nTOTAL: R${:.2f}'.format(com_juros))
    else:
        print('\033[1;31mOPÇÃO INVALIDA! Tente novamente!')
else:
    print('\033[1;31mOPÇÃO INVALIDA! Tente novamente!')

"""
        #A louca complicando tudo, eoheom
        if parcelas == 3:
            divisão = com_juros / 3
            print('3X DE {:.2f} C/JUROS'.format(divisão),
                  '\nTOTAL: R${:.2f}'.format(com_juros))
        elif parcelas == 4:
            divisão = com_juros / 4
            print('4X DE {:.2f} C/JUROS'.format(divisão),
                  '\nTOTAL: R${:.2f}'.format(com_juros))
        elif parcelas == 5:
            divisão = com_juros / 5
            print('5X DE {:.2f} C/JUROS'.format(divisão),
                  '\nTOTAL: R${:.2f}'.format(com_juros))
        elif parcelas == 6:
            divisão = com_juros / 6
            print('6X DE {:.2f} C/JUROS'.format(divisão),
                  '\nTOTAL: R${:.2f}'.format(com_juros))
        elif parcelas == 7:
            divisão = com_juros / 7
            print('7X DE {:.2f} C/JUROS'.format(divisão),
                  '\nTOTAL: R${:.2f}'.format(com_juros))
        elif parcelas == 8:
            divisão = com_juros / 8
            print('8X DE {:.2f} C/JUROS'.format(divisão),
                  '\nTOTAL: R${:.2f}'.format(com_juros))
        elif parcelas == 9:
            divisão = com_juros / 9
            print('9X DE {:.2f} C/JUROS'.format(divisão),
                  '\nTOTAL: R${:.2f}'.format(com_juros))
        elif parcelas == 10:
            divisão = com_juros / 10
            print('10X DE {:.2f} C/JUROS'.format(divisão),
                  '\nTOTAL: R${:.2f}'.format(com_juros))

"""

# Resolução da aula

#print('(:=^40)'.format(' LOJAS GUANABARA '))
# esse ^ significa que 'LOjas guanabara' será centralizado em 40 espaços
