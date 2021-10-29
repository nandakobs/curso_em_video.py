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
    #
    # min 20
print('FIM')
