def aumentar(preco, porcentagem, formata=True):
    aumento = preco + (preco * porcentagem/100)
    if formata:
        aumento = f'R${aumento:.2f}'.replace('.', ',')
    return aumento


def diminuir(preco, porcentagem, formata=True):
    desconto = preco - (preco * porcentagem/100)
    if formata:
        desconto = f'R${desconto:.2f}'.replace('.', ',')
    return desconto


def dobro(n, formata=True):
    n *= 2
    if formata:
        n = f'R${n:.2f}'.replace('.', ',')
    return n


def metade(n, formata=True):
    n = n / 2
    if formata:
        n = f'R${n:.2f}'.replace('.', ',')
    return n


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


def resumo(preco=0, aumento=10, desconto=5):
    print('=' * 30)
    print('{:^30}'.format('RESUMO DO VALOR'))
    print('=' * 30)
    print(f'Preço analisado:     {moeda(preco)}')
    print(f'Dobro do preço:      {dobro(preco)}')
    print(f'Metade do preço:     {metade(preco)}')
    print(f'{aumento}% de aumento:      {aumentar(preco, aumento)}')
    print(f'{desconto}% de redução:      {diminuir(preco, desconto)}')
    print('=' * 30)


# Resolução das aulas
def funcao(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    print(f'Metade do preço:     \t{metade(preco)}')
    # \t (contra-barra t) para tabulação
    return res if formato is False else moeda(res)
