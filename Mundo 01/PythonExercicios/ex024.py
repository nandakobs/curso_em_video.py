cidade = input('Digite o nome de uma cidade: ').upper().split()
print('Começa com SANTO? {}'.format('SANTO' in cidade[0]))

#Resolução da aula
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')