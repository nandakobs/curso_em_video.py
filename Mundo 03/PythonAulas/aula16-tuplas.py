"""
Em Python existem 3 tipos de variaveis compostas: tuplas, listas e dicionarios
Variavei simples armazenam apenas um valor, variaveis compostas armazenam varios
simples = suco
composta = (suco, burguer, batata frita)
compostas = (tupla) [lista] {dicionario}
>>>> TUPLAS

> Como posso acessar um elemento dentro de uma tupla?
    Esses elemento são identificados por indices númericos, que começam
    em zero (assim como numa array).

strings são variaveis compostas
lanche = burguer, suco, pizza, pudim
print(lanche[2])    # pizza
print(lanche[0:2])  # burguer e suco # ultimo elemnto nunca é contado
print(lanche[1:])   # suco e tds os outros elemntos até o final (pizza e pudim)
print(lanche[-1])   # ultimo elemento (pudim) (-4 é o burguer)
len(lanche)         # quantos elementos tem lanche? 4
for c in lanche:    # imprime cada elemento de lanche
    print(c)

TUPLAS SÃO IMUTÁVEIS
Eu não consigo atribuir valores a tupla a não ser na declaração dela

Posso ter varios tipos dentro de uma tupla: str, int, float e etc

"""
lanche = ('burguer', 'suco', 'pizza', 'pudim', 'batata frita')
# da pra fazer uma tupla sem () mas vamos manter a organização plmds
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(lanche[2:])
print(lanche[-3:])

for comida in lanche:
    print(f'Eu vou comer {comida}')
# OU
for cont in range(0, len(lanche)):
    print(cont)  # imprimiria de 0 a 4, pois range n conta com o ultimo n°
    print(f'Vou comer {lanche[cont]} na posição {cont}')  # imprime tds os nomes
# OU
for pos, comida in enumerate(lanche):  # pos seria o cont
    print(f'Comerei {comida} na posição {pos}')
print('Comi pra caramba!')

print(sorted(lanche))  # Organizei em ordem alfabetica
print(lanche)  # mas lanche não se modificou, apenas mostrei diferente

a = (5, 2, 4)
b = (5, 8, 1, 1, 2)
c = a + b
d = b + a  # diferente de a + b
print(c)
# Ele literalmente junta, vem a e dps começa b
print(c.count(5))  # quantas vezes aparece o n° 5 em c?
print(c.index(8))  # em que posição está o n° 8 em c?
# Se o n° aparecer mais de uma vez na tupla, ele retorna a 1ª posição
print(c.index(5, 1))  # a partir da posição 1, onde mais tem 5?

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)  # deleta a tupla AHAHAH
# Então a tupla é imutável a menos que vc apague ela INTEIRA
# del(pessoa[0]) NÃO da certo
print(pessoa)