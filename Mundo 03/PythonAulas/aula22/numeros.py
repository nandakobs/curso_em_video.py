#import uteis  #pra modulo sendo arquivo ao lado
from uteis import numeros  #pra modulo em um pacote
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')