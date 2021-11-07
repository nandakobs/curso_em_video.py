"""
Os dicionários são variáveis compostas que permitem
armazenar vários valores em uma mesma estrutura,
acessíveis por chaves literais.

Dicionários são identificados por chaves {}
dados = dict() ou dados = {}

"""
lista = ['Pedro', 25]
print(lista[0])  # Pedro
print(lista[1])  # 25
dicio = {'nome': 'Pedro', 'idade': 25}
print(dicio['nome'])   # Pedro
print(dicio['idade'])  # 25
dicio['sexo'] = 'M'  # Adiciona sexo: M no final do dicionario
del dicio['idade']  # Remove idade: 25

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}
# Valor, Chaves e Itens
print(filme.values())  # dict_values(['Star Wars', 1977, 'George Lucas'])
print(filme.keys())  # dict_keys(['titulo', 'ano', 'diretor'])
print(filme.items())  # dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])

for chave, valor in filme.items():
    print(f'O {chave} é {valor}')
    """O titulo é Star Wars
       O ano é 1977
       O diretor é George Lucas"""

# locadora é uma lista com dicionários(filmes) dentro dela
locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
            {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Mhedon'},
            {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Machowski'}]
print(locadora[0]['ano'])  # 1977
print(locadora[2]['titulo'])  # Matrix


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])  # Gustavo
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')  # O Gustavo tem 22 anos.

print(pessoas.items())
# dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])
# Perceba que ele colocou os items dentro de uma lista []
# e essa lista é composta de 3 tuplas ()


for k in pessoas.keys():
    print(k)
    """
    nome
    sexo
    idade
    """
for v in pessoas.values():
    print(v)
    """
    Gustavo
    M
    22
    """
for i in pessoas.items():
    print(i)
    """
    ('nome', 'Gustavo')
    ('sexo', 'M')
    ('idade', 22)
    """
for k, v in pessoas.items():
    print(f'{k} = {v}')
    """
    nome = Gustavo
    sexo = M
    idade = 22
    """


pessoas['nome'] = 'Leandro'  # troca Gustavo por Leandro
pessoas['peso'] = 98.5  # Adiciona peso no final do dicionario
print(pessoas)  # {'nome': 'Leandro', 'sexo': 'M', 'idade': 22, 'peso': 98.5}


brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)  # brasil é uma lista com 2 dicionarios
# [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
print(brasil[0]['uf'])  # Rio de Janeiro
print(brasil[1]['sigla'])  # SP

estado = dict()
brazil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brazil.append(estado.copy())
print(brazil)  # [{'uf': 'Acre', 'sigla': 'AC'}, {'uf': 'Sergipe', 'sigla': 'SE'}, {'uf': 'Bahia', 'sigla': 'BA'}]
for e in brazil:
    print(e)
    """
    {'uf': 'Acre', 'sigla': 'AC'}
    {'uf': 'Sergipe', 'sigla': 'SE'}
    {'uf': 'Bahia', 'sigla': 'BA'}
    """
for e in brazil:
    for chave, valor in e.items():
        print(f'O campo {chave} tem valor {valor}')
        """
        O campo uf tem valor Acre
        O campo sigla tem valor AC
        O campo uf tem valor Sergipe
        O campo sigla tem valor SE
        O campo uf tem valor Bahia
        O campo sigla tem valor BA
        """
    for valor in e.values():
        print(valor, end=' ')
    print()
    """
    Acre AC
    Sergipe SE
    Bahia BA
    """
#min 33:55