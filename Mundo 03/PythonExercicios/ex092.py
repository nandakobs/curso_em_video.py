from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - nasc
pessoa['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    # levando em consideração aposentaria = 35 de contribuição
    # com quantos anos a pessoa vai se aposentar
    contrib = date.today().year - pessoa['contratação']
    if contrib == 35:
        pessoa['aposentadoria'] = pessoa['idade']
    elif contrib < 35:
        apos = 35 - contrib
        pessoa['aposentadoria'] = apos + pessoa['idade']
    elif contrib > 35:
        apos = contrib - 35
        pessoa['aposentadoria'] = pessoa['idade'] - apos
print('=' * 30)
# print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem valor {v}')

# Resolução da aula
# dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year())
