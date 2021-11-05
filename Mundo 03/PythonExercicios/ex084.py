"""# 70 < leve
people = []
lista = []
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    people.append(lista[:])
    lista.clear()
    continua = ''
    while 'S' != continua != 'N':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
leves = []
pesados = []
mais_leve = mais_pesado = 0
p_leve = p_pesado = ''
for pos in people:
    if pos[1] <= 70:
        leves.append(pos[0])
    else:
        pesados.append(pos[0])
    if pos == 0:
        p_leve = pos[0]
        mais_leve = pos[1]
        p_pesado = pos[0]
        mais_pesado = pos[1]
    if pos[1] < mais_leve:
        mais_leve = pos[1]
        p_leve = pos[0]
    if pos[1] > mais_pesado:
        mais_pesado = pos[1]
        p_pesado = pos[0]

print(people, '\n', leves, '\n', pesados)

print('='*50)
print(f'Foram cadastradas {len(people)} pessoas.')
print(f'Os pesos leves são {leves} sendo {p_leve} mais leve que todos com {mais_leve}KG.')
print(f'Os pesos pesados são {pesados} sendo {p_pesado} mais pesado que todos com {mais_pesado}KG.')
"""
# Resolução da aula

temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar: [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
#print(f'Os dados foram {princ}')
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}, ', end='')
print()
print(f'O menor peso foi de {menor}Kg.Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}, ', end='')
