"""
# INTERACTIVE HELP

Python sendo o cheiroso que é, tem ajuda interativa.
Abra o Python Console e digite: help()
Após, se você digitar por exemplo, print
Ele te diz o que é o print e suas keywords/parametros(ex: end='')
Além das funcionalidades built-in, você pode tbm consultar a documentação de lib's baixadas.
Digite quit pra sair.

If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
As an example run: help(print)

Você também pode imprimir o doc interno dentro de um comando, com:
print(sum.__doc__)



# DOCSTRINGS

Você não será a unica pessoa a ler e usar o seu codigo;
imagine ter de descobrir o que uma função que não foi
criada por você faz? Para isso existem docstrings.
Elas são declaradas logo abaixo do comando def,
abra 3 aspas duplas e de enter para criar uma docstring.
Assim, você ou outras pessoas poderão utilizar
help(nome_da_def)
pra saber pra que ela serve.
"""

# DOCSTRINGS
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do CursoEmVideo.
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


contador(0, 10, 2)
help(contador)

"""

# PARÂMETROS OPCIONAIS

Vimos na aula passada que se uma função tem 3 parâmetros
e ao chama-la passamos apenas 2, ela dará erro. Porém,
se declararmos que um parâmetro recebe 0 (zero) e ao
chamar a função não atribuímos um valor a este parâmetro
então ele ainda funcionará, pois o parâmetro ainda tem valor.

def somar(a, b, c = 0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)  # Com o parâmetro opcional, isso aqui funciona

Nada lhe impede de fazer def somar(a=0, b=0, c=0):
somar(b=4, c=2)  # tbm funfa
Assim chamar a função vazia: somar(), tbm funcionaria
Note que se você tentar somar 4 números, não dará certo
pois não se pode ultrapassar o limite de parâmetros definidos.


# ESCOPO DE VARIÁVEIS

Basicamente na programação escopo é o local onde uma 
variavel vai existir e o local onde a variavel não vai
mais existir.
"""
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
# print(f'No programa principal, chamar {x} da erro')
teste()

# Aqui n é um escopo global
# Mas x é um escopo local, pois só existe dentro da função


# PECULIARIDADES DE PYTHON

# ========================= ESCOPO GLOBAL ===
# ========= ESCOPO LOCAL ============       #
def test3(b):                       #       #
    b += 4                          #       #
    c = 2                           #       #
    print(f'A dentro vale {a}')     #       #
    print(f'B dentro vale {b}')     #       #
    print(f'C dentro vale {c}')     #       #
# ===================================       #
                                            #
                                            #
a = 5                                       #
test3(a)                                    #
print(f'A fora vale {a}')                   #
# ===========================================
"""
Ao chamar test3(a), copiamos o valor da variavel
de escopo global, a, para o parâmetro da função test3
que é b.
Dentro da função, b tem seu valor adicionado a 4
e passa a valer 9. C é igual a 2. Até então todos
os prints retornarão:
A dentro vale 5  # pois é uma variavel de escopo global
B dentro vale 9
C dentro vale 2
A fora vale 5

>>>>> PORÉM
Se eu declarar dentro da função que a = 8,
o valor de a, a variavel de escopo global,
permanece 5. Pois freaking Python CRIOU
a variavel a dentro da função. Os prints
retornarão o seguinte:
A dentro vale 8   # pois Python criou
B dentro vale 9
C dentro vale 2
A fora vale 5    # a de escopo global permanece inalterada

>>>>> PORÉM
Se eu digo:

def test3(b):
    global a
    a = 8                       
    b += 4                          
    c = 2                           
    print(f'A dentro vale {a}')     
    print(f'B dentro vale {b}')     
    print(f'C dentro vale {c}') 
    
Esse global a diz ao Python:
PELO AMOR DE DEUS NÃO CRIA OUTRA VARIAVEL, A É GLOBAL
Então Python não cria uma variavel dentro da função.
Assim a, variavel de escopo global, agora vale 8.
Os prints retornarão:
A dentro vale 8   # global a
B dentro vale 9
C dentro vale 2
A fora vale 8     # global a


# RETORNANDO VALORES

O famoso return.
Funções que retornam resultados são muito uteis
quando eu quero ter personalização dos resultados.
Recebe numeros, strings, bool, listas, tupla, dicios e etc

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
"""


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')