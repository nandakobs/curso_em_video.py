sexo = ''
while 'M' != sexo != 'F':
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    if 'M' != sexo != 'F':
        print('Resposta Inválida!\nDigite F para feminino e M para masculino\n')
print('Sexo Feminino' if sexo == 'F' else 'Sexo Masculino')

#OU

sexo = str(input('Sexo: [M/F] ')).upper().strip()
while 'M' != sexo != 'F':
    print('Resposta Inválida!\nDigite F para feminino e M para masculino\n')
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
print('Sexo Feminino' if sexo == 'F' else 'Sexo Masculino')

"""
# Resolução da aula

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper[0] # [0] pega apenas a primeira letra
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
"""