"""
frase = 'Curso em Video Python'

O programa armazena em "mini espaços" dentro do pc
C u r s o   e m   v i d e o      P y t h o n
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
São 21 espaços, assim como em arrays começa no Zero

Fatiamento de strings

frase[9]
lista, mostraria a letra V

frase[9:13]
mostra da posição 9 a 13, excluindo a 13
mostraria Vide
pra mostrar Video, seria de 9 a 14

frase[9:21]
como acaba em 20, 21 mostra Video Python

frase[9:21:2]
mostra de 9 a 20, pulando de 2 em 2
mostraria V d o P t o

frase[:5]
Quando omitido o começo ele começa do elemento zero
mostraria Curso

frase[15:]
Quando omitido o final, ele vai do elemento especificado até o final
mostraria Python

frase[9::3]
Vai de 9 até o final da string, pulando de 3 em 3
mostraria V e P h

## Analisando strings ##

len(frase)
length = retorna o comprimento da frase
mostraria 21(caracteres)

frase.count('o')
Neste caso, ele conta quantas vezes a letra o minuscula aparece em frase
mostraria 3

frase.count('o',0,13)
Contagem com fatiamento
conta aparições de 'o' entre elementos de 0 a 13
mostraria 1 (ultimo valor sempre é ignorado - se n seria 2)

frase.find('deo')
Ele encontra o que você pede e mostra posição inicial
mostraria a posição 11 (onde começa deo)

frase.find('Android')
No caso, 'Android' não existe em frase
ele retorna -1, pois não existe na string

'Curso' in frase
Existe a palavra Curso em frase?
Retorna:
True, se sim
False, se não

## Transformação ##

Via de regra, uma lista de string é imutável
não se consegue mudar diretamente os elementos
mas podemos mudar através de uma função de string
e fazer uma atribuição (depositar numa variável)

frase.replace('Python','Android')
substitui primeiro elemento pelo segundo
então ficaria:
frase = Curso em Video Android

frase.upper()
Toda a string fica em letras maiúsculas

frase.lower()
Toda a string fica em letras minusculas

frase.capitalize()
A primeira letra da string ficará em maiúsculo
e todo o resto em minusculo

frase.title()
O title reconhece palavras pelo espaço em branco
entre elas e coloca a primeira letra de cada palavra
em maiúsculo


frase =   Aprenda Python
       123 45678910 11 121314151617 1819
Algumas pessoas colocam espaços para verificar se esta
funcionando em antes e depois de responder, para
corrigir isso usamos:

frase.strip()
remove todos os espaços inúteis no começo e na final da string

frase.rstrip()
Esse r é de right, começa a tratar pela direita
e nesse caso só remove os espaços inúteis do final

frase.lstrip()
Esse l é de left, começa a tratar pela esquerda
e nesse caso só remove os espaços inúteis do começo


frase = Curso em Video Python

frase.split()
gera uma lista, separando os itens por default pelo
espaço em branco. Ficaria:
frase = ['Curso', 'em', 'Video', 'Python']

'-'.join(frase)
Junta a lista frase em uma só string. Mostraria:
Curso-em-Video-Python

"""
frase = 'Curso em Video Python'
print(frase)
print(len(frase), 'caracteres')
print(frase.replace('Python', 'Android'))
print('='*20)

print(frase.find("Curso"))
print('Curso' in frase)
print('Guanabara' in frase)
print(frase.find('Video'))
print(frase.find('video'))
print(frase.lower().find('video'))
print('='*20)

dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2])
print(dividido[2][3])
# me mostra elemento 2 da lista, caractere 3 do elemento
print('='*20)


print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print('='*20)

print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print('='*20)

print('oi')
#Mas e se for um texto longo?
print("""Mussum Ipsum, cacilds vidis litro abertis.
Manduma pindureta quium dia nois paga. In elementis 
mé pra quem é amistosis quis leo. Delegadis gente 
finis, bibendum egestas augue arcu ut est. 
Tá deprimidis, eu conheço uma cachacis que pode 
alegrar sua vidis.""")