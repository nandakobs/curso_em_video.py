from math import radians, cos, sin, tan
angulo = float(input('Qual é o ângulo? '))
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))

"""cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))"""

print('O ângulo {} tem seno de {:.4f}, cosseno de {:.4f} e tangente de {:.4f}'.format(angulo, seno, cosseno, tangente))
