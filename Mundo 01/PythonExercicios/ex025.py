nome = input('Digite seu nome completo: ').upper()
print('Sobrenome Silva no nome? {}'.format('SILVA' in nome))

# Resolução da aula
nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
