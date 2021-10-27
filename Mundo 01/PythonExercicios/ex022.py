nome = input('Qual é o seu nome completo? ').strip()
print(nome.upper())
print(nome.lower())
num_nome = len(''.join(nome.strip()))-1
print('São {} letras ao todo.'.format(num_nome))
first_name = nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(first_name[0])))


"""
Resolução da aula: 

nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
"""