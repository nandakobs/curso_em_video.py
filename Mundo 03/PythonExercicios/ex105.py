def notas(*n, situ=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param situ: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    boletim = {'Quantidade de notas': len(n),
               'A maior nota': max(n),
               'A menor nota': min(n),
               'Média das notas': sum(n) / len(n)}
    if situ:
        if boletim['Média das notas'] >= 7:
            boletim['Situação'] = 'BOA'
        elif 5 >= boletim['Média das notas'] < 7:
            boletim['Situação'] = 'RAZOAVEL'
        else:
            boletim['Situação'] = 'RUIM'
    return boletim


resp = notas(5.5, 9.5, 10, 6.5, situ=True)
resp2 = notas(5, 3, 0, 6.5)
print(resp, resp2)
help(notas)