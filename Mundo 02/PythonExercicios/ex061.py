primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + 8 * razão # definindo o decimo termo, onde para de contar
pa = [primeiro, ]
c = primeiro
while c != decimo + razão:
    c = c + razão
    pa.append(c)
separator = ', '
print('Os dez primeiros termos são {}'.format(separator.join(map(str, pa))))

"""
# Resolução da aula

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão de PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')

"""