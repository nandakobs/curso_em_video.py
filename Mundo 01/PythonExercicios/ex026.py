frase = input('Diga ai uma frase: ').lower().strip()
print('Sua frase tem {} letras A'.format(frase.count('a')))
print('A letra A aparece pela 1° vez na posição: {}'.format(frase.find('a')))
print('A letra A aparece pela ultima vez na posição: {}'.format(frase.rfind('a')))

#Prof adicionou +1 nos ultimos dos format pra fazer sentido para o usuario