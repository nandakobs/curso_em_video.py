"""
Digamos que temos uma biblioteca(lista(de funções)) de bebidas, como:
bebidas = [suco, agua, café, refri]
se eu disser
import bebidas
no começo do arquivo então o python vai carregar tds as bebidas pra q
eu possa usar. Mas e se eu só quiser o café?
from bebidas import café

Vamos falar de uma biblioteca muito conhecida no python
math
Essa biblioteca traz uma lista de funções matematicas adicionais, tais como:
ceil = arredonda pra cima
floor = arredonda pra baixo
trunc = elimina da virgula pra frente
pow = de power > potencia
sqrt = square root > raiz quadrada
factorial = fatorial

import math >> importa todaaas as funções
from math import sqrt >> só posso usar sqrt
from math import sqrt, ceil >> posso usar sqrt e ceil

"""
"""import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

#quando eu importo algo diretamente n preciso usar  math. pra chamar a função
from math import sqrt
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))"""

# você pode ver quais modulos vc pode importar no site oficial do python
# docs > library references
# na biblioteca random eu posso gerar numeros aleatorios
import random
num = random.random()
#o metodo random da classe random gera um numero aleatorio entre 0 e 1
num2 = random.randint(1, 10)
#gera um numero inteiro aleatorio entre 1 e 10
print(num, '\n', num2)

# em PyPi no site oficial de Python temos a lista de pacotes extras q vc pode importar

import emoji
print(emoji.emojize('Olá, mundo :globe_showing_Americas:', use_aliases=True))

# Settings > Project > Python Interpreter pra ver os modulos q vc já tem ou add ou desistala por la

