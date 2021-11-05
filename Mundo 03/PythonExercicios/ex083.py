frase = list(str(input('Digite uma expressão: ')))
#print(frase)
abre = fecha = 0
for c in frase:
    if c == '(':
        abre += 1
    if c == ')':
        fecha += 1
print('Expressão válida!' if abre == fecha else 'Expressão inválida!')