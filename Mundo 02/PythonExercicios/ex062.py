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
mais_termos = int(input('Quantos termos a mais você quer ver? '))
c = pa[len(pa)-1]
termos = c + (mais_termos - 1) * razão
while mais_termos != 0:
    while c != termos + razão:
        c = c + razão
        pa.append(c)
    separator = ', '
    print('Os próximos {} termos são {}'.format(mais_termos, separator.join(map(str, pa[(len(pa) - mais_termos)::]))))
    mais_termos = int(input('Quantos termos a mais você quer ver? '))
    c = pa[len(pa) - 1]
    termos = c + (mais_termos - 1) * razão
print('\n===== CALCULADORA DE PA ENCERRADA =====')

"""#Resolução da aula

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão de PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

"""