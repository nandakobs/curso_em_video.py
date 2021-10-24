n = int(input('Digite um numero: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('O dobro de {} é {}, \no triplo é {}, \ne sua raiz quadrada é {:.2f}'.format(n, dobro, triplo, raiz))

'''
Assim como no exercicio anterior vc pode fazer td no print
print('O dobro de {} é {}, \no triplo é {}, \ne sua raiz quadrada é {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))))
lembrando que a raiz quadrada tbm da pra fazer com pow
pow(n, (1/2))
'''