#Operações Aritimeticas
# +  Adição
# -  Subtração
# *  Multiplicação
# /  Divisão
# ** Potencia ou pow(2,4)
# // Divisão inteira
# %  Resto da Divisão

# Ordem de precedencia
# 1° ()
# 2° **
# 3° * / // %
# 4° + -

#Calcular a raiz quadrada de um numero é a mesma coisa q criar a
# potencia dele por meio, ou seja
raizquadrada = 81**(1/2) #é nove
raizcubica = 127**(1/3)

print('oi'*5) #escreve oi 5 vezes

nome = input('Qual é seu nome?')
print('Prazer em te conhecer {:=^20}!'.format(nome))
#{:20} faz com que o nome apareça em 20 caracteres
# Se eu botar o sinal de maior >, eu alinho o que tá escrito a direita
# < para alinhar a esquerda
# ^ para centralizar
# se você botar = em antes do sinal, ele preencherá os espaços em branco com =

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))
soma = n1 + n2
vezes = n1 * n2
dividi = n1 / n2
div_inteira = n1 // n2
expo = n1 ** n2
#                    em divisão: formatando pra q apareça 3 casas decimais flutuantes
print('A soma é {},\n o produto é {} \ne a divisão é {:.3f}'.format(soma, vezes, dividi), end = ' ')
print('Divisão inteira é {} e potência é {}'.format(div_inteira, expo))
#pra não quebrar a linha entre um print e outro use (, end = '') no final da 1°
# pra quebrar a linha no print digite \n



