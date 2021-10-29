"""
if carro.esquerda():
    [bloco de codigo]
elif carro.direita():
    [bloco de codigo]
elif carro.ré():
    [bloco de codigo]
else:
    [bloco de codigo]
"""

nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
elif nome == 'Fernanda':
    print('Tens o nome mais lindo do mundo!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
