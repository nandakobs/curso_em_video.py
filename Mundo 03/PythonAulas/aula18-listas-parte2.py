"""
Listas compostas são listas dentro de listas

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])  # Pedro
print(pessoas[1][1])  # 19
print(pessoas[2][0])  # João
print(pessoas[1])     # ['Maria', 19]

"""
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
# Você espera que o print retorne [['Gustavo', 40], ['Maria', 22]], não é?
# mas na vdd ele retorna [['Maria', 22], ['Maria', 22]]
# pois não fizemos uma copia da lista teste, só atribuimos seu valor a galera
# O jeito que dá certo é:
t3ste = list()
t3ste.append('Gustavo')
t3ste.append(40)
gal3ra = list()
gal3ra.append(t3ste[:])
t3ste[0] = 'Maria'
t3ste[1] = 22
gal3ra.append(t3ste)  # Eai colocar [:] aqui se for modificar as posições 1 e 0 dnv
print(gal3ra)

print('='*50)

galere = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galere:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print('='*50)

g4lera =list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    g4lera.append(dado[:])
    dado.clear()  # apaga tudo
print(g4lera)
maiores = menores = 0
for p in g4lera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maiores += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menores += 1
print(f'Temos {maiores} maiores e {menores} menores de idade.')
