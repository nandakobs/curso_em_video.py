frase = str(input('Diga uma frase ai: ')).replace(' ', '')
palindromo = frase[::-1]
if frase == palindromo:
    print('É UM PALINDROMO!\n'
          '{} ao contrário é {}'.format(frase, palindromo))
else:
    print('NÃO É UM PALINDROMO!\n'
          '{} ao contrário é {}'.format(frase, palindromo))


# Resolução da aula
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')