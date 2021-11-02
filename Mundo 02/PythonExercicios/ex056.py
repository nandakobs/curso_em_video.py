"""
nomes = []
idades = []
sexos = []
for c in range(4):
    nome = str(input('Qual é o seu nome?')).strip()
    idade = int(input('Quantos anos você tem?'))
    sexo = str(input('És do sexo masculino ou feminino? [M/F]')).upper()
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

print(nomes, idades, sexos)

media = (idades[0] + idades[1] + idades[2] + idades[3]) / 4
print('A média de idade do grupo é: {}'.format(media))
"""


"""
# Tentativa 01 - erro
velho = []
novinhas = []
velho[0] = sexos[0] if sexos[0] == 'M' else novinhas[0] = sexos[0]
velho[1] = sexos[1] if sexos[1] == 'M' else novinhas[1] = sexos[1]
velho[2] = sexos[2] if sexos[2] == 'M' else novinhas[2] = sexos[2]
velho[3] = sexos[3] if sexos[3] == 'M' else novinhas[3] = sexos[3]
velhote = velho.index(max(velho))s
print('O nome do homem mais velho é: {}'.format(nomes[velhote]))

# Tentativa 02 - erro

if idades[min(idades)] == 'M' in sexos[min(idades)]:
    print(nomes[min(idades)])

"""

# Resolução da aula

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher20 += 1

media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_velho))
print('Ao todo são {}  mulheres com menos de 20 anos.'.format(tot_mulher20))








