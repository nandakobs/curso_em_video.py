"""
Que coisas você faz constantemente?
Funções estão ligadas a rotinas.
Você ainda não percebeu mas já usou várias funções
built-in do Python: print(), input(), int(), len()...
Tudo isso são FUNÇÕES!
Mas então que tipo de função VOCÊ poderia criar?
Uma função que não existe no Python, mas que
vai ser personalizada a sua necessidade (pq vc usa muito).
Sabe aquelas linhas de código que você tem que repetir de novo
e de novo e de novo no seu código? Crie uma função pra ela!
Assim você otimiza seu tempo e deixa seu código mais limpo.

def == definição de função

Uma função só é executada quando chamada.
Depois de uma função vc tem que pular 2 linhas.
Funções devem ser declaradas no começo, acima do programa principal

# Em vez de:
print('-' * 30)
print('  CURSO EM VIDEO')
print('-' * 30)
print('-' * 30)
print('  CURSO DE PYTHON  ')
print('-' * 30)
print('-' * 30)
print('  GUANABARA  ')
print('-' * 30)
# Faça:
def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem('CURSO EM VIDEO')
mensagem('CURSO DE PYTHON')
mensagem('GUANABARA')



# Em vez de:
a = 4
b = 5
s = a + b
print(s)
c = 8
d = 9
s = a + b
print(s)
e = 2
f = 1
s = a + b
print(s)
# Faça:
def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

soma(7, 2)
soma(a=4, b=5)  # você pode deixar explicitar assim
# soma(a=4, 5) MAS isso aqui da erro, se explicitar 1, faça com tds
soma(3, 9, 8)  # Isso aqi da erro pois vc definiu apenas 2 parametros


# EMPACOTAR E DESEMPACOTAR
Vamos dizer que você fazer uma função q conte numeros
a 1° entrada: contador(5, 7, 3, 1, 4)
a 2° entrada: contador(8, 4, 7)
Como fazer essa função da certo?

def contador(*num)
Esse asterisco significa desempacotar.
Tu tá dizendo pro Python:
Ó, o usuario vai te passar uns numeros ai, não sei quantos são
mas o que ele te passar tu armazena ai em num
"""
def contador(*num):
    print(num)
    # VIRAM TUPLAS
    for valor in num:
        print(f'{valor}', end=' ')
    print('FIM')
    print(f'Recebi os valores {num} e são ao todo {len(num)} números.')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 9, 2)



def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)  # [14, 4, 10, 0, 8]



def soma(*valores):  # varios valores
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
soma(6, 8, 10, 12)
soma(1999, 1)

