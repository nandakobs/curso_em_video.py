"""
laço c no intervalo(1, 10) #de 1 a 10
    passo
pega

for c in range(1, 10):
    passo
pega


laço c no intervalo(0, 3)
    passo
    pula
passo
pega

for c in range(0, 3):
    if moeda:
        pega
    passo
    pula
passo
pega

"""
# você pode chamar esse c de qualquer coisa
for c in range(1, 6):
    print('oi', c)
    # só imprimi 5 oi's, pq ele faz de 1 até 5 e no 6 ele para
    # ele nunca considera/faz o ultimo numero
print('FIM')

for c in range(6, 0, -1):
    print('oi', c)
    # Faz conta pra trás, precisa do -1
    # Se colocar 2 no lugar do -1, ele irá contar pulando de 2 em 2
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n+1):  # sem esse +1 ele faria até um numero em antes do colocado
    print(c)
print('FIM')

i = int(input('Inicio: '))  # valor do começo da contagem
f = int(input('Fim: '))  # valor do fim da contagem
p = int(input('Passo: '))  # valor de como será contado
for c in range(i, f+1, p):  # muda pra -1 pra contagem regressiva dar certo
    print(c)
print('FIM')


soma = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    soma += n  # soma = soma + n
# n é repetido 4 vezes e dps soma os 4 valores recebidos
# mas quando dou print no valor de n aparece o ultimo n° digitado
# Se ele guardou os 4 valores inseridos e foi capaz de soma-los
# quando eu dou print nele, não deveria mostrar esses 4 valores?
# ME AUTO RESPONDENDO AQUI:
# é um looping, ou seja n recebe valor e passa pra soma,
# quando n recebe um segundo valor, soma já tem o valor do primeiro
print(n)
print('O somatório de todos os valores foi {}'.format(soma))



