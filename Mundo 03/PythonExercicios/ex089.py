# lista = [['aluno', [5.0, 4.0]], ]
alunos = []
cont = 0
while True:
    alunos.append([str(input('Nome: '))])
    alunos[cont].insert(1, [float(input('Nota 1: ')), float(input('Nota 2: '))])
    cont += 1
    continua = ''
    while 'S' != continua != 'N':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('-='*30)
# print(alunos)
print('N°. NOME           MÉDIA')
print('-='*30)
conta = 0
for c in alunos:
    print(f'{conta}   {c[0]}          {sum(c[1])/2:.1f}')
    conta += 1
while True:
    notas = int(input('Mostrar as notas de qual aluno? (999 p/ SAIR) '))
    if notas == 999:
        break
    print(f'Notas de {alunos[notas][0]} são {alunos[notas][1]}')
print('Finalizando....')
print('<<<<< VOLTE SEMPRE >>>>>>')

# Resolução da aula

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"N°.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')