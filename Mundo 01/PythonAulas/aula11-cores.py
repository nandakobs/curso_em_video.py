"""
Pesquisar modulo colorize

ANSI - escape sequence
Sempre que você quiser colocar uma cor em Python
você vai começar com \033[m
Entre o colchete [ e o m podemos colocar
\033[style;text;backm
style: codigo do estilo (normal, negrito, sublinhada)
text:  codigo do texto  (cor do texto)
back: de background, codigo de cor de fundo (cor do fundo)
Na vdd, vc pode colocar em qualquer ordem pois tu vai notar
que existe uma diferença entre cada tipo de codigo
Exemplo: \033[0;33;44m

style: 0 - None, 1 - Bold, 4 - Underline, 7 - Negative

text:              back:
 30   - Branco   -   40
 31   - Vermelho -   41
 32   - Verde    -   42
 33   - Amarelo  -   43
 34   - Azul     -   44
 35   - Magenta  -   45
 36   - Ciano    -   46
 37   - Cinza    -   47

"""
print('\033[31mOlá, Mundo!')
print('\033[1;35mOLHA ISSO AQUI EM ROXO')
print('\033[1;33m-=-' * 10)
print('\033[1;30;46mOLHA ESTE FUNDINHO\033[m')
print('\033[7;37mNEGATIVE\033[m')
a = 3
b = 5
print('Os valores são \033[33m{}\033[m e \033[34m{}\033[m'.format(a, b))

nome = 'Guanabara'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'brancoepreto': '\033[7;30m'}
print('Olá,{}{}{}!!'.format('\033[36m', nome, '\033[m'))
print('Tu é dez, {}{}{}!!'.format(cores['brancoepreto'], nome, cores['limpa']))

#Desafio1 = dos 35, pegue 10 e coloque cores
#Desafio2 = nos 35, crie um sistema de cores pra ele
