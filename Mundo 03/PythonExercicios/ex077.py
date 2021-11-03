tupla = ('Fernanda', 'Mariana', 'Juliana', 'Daiane', 'Joana', 'Eliana')

"""for c in range(len(tupla)):
    analise = tupla[c]
    analise = analise.lower()
    print(f'{tupla[c]} tem as vogais ', end='')
    if 'a' in analise:
        print('a', end=' ')
    if 'e' in analise:
        print('e', end=' ')
    if 'i' in analise:
        print('i', end=' ')
    if 'o' in analise:
        print('o', end=' ')
    if 'u' in analise:
        print('u', end=' ')
    print('\n', '=' * 30)"""

# Resolução da aula

for p in tupla:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'áãâéêíõóaeiou':
            print(letra, end=' ')
