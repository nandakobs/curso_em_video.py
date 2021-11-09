from datetime import date


def voto(i):
    if i < 16:
        return 'VOTO NEGADO'
    elif 16 <= i < 18 or i > 65:
        return 'VOTO OPCIONAL'
    elif i > 18:
        return 'VOTO OBRIGATÓRIO'


nasc = date.today().year - int(input('Em que ano você nasceu?'))
print(f'Com {nasc} anos: {voto(nasc)}.')

"""# Resolução da aula
def voto(ano):
    from datetime import date  # se é usado somente na função importe dentro dela, economiza espaço
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))"""