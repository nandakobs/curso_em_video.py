def fatorial(numero=1, show=True):
    """
    -> Calcula o fatorial de um numero
    :param numero: O numero a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: O valor do fatorial da variável numero
    """
    f = 1
    for c in range(numero, 0, -1):
        f *= c
    if show:
        for k in range(numero, 0, -1):
            print(f'{k}', end='')
            print(' x ' if k > 1 else ' = ', end='')
        print(f)
    else:
        return f


print(fatorial(5, False))
help(fatorial)


"""
# Resolução da aula
f = 1
for c in range(numero, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
"""