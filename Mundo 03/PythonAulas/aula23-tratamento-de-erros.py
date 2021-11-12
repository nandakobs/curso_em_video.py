"""
Erro de sintaxe é quando você escreve algo errado,
endentação errada, comando escrito errado e etc.

Erros de exceções são erros de lógica, como por exemplo
um int(input()) receber uma string dá ValueError.

"""
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'Problema encontrada foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:  # dando erro ou não isso aqui irá acontecer no final
    print('Volte sempre! Muito obrigada!')

"""
else e finally são opcionais.

Todo try pode ter mais de 1 except.
try:
    tal comando
except ValueError:
    tal comando
except TypeError:
    tal comando
"""