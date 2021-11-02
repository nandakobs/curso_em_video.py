n = soma = conta = 0
print('Me diga quantos números você quiser, para parar digite 999')
print('='*60)
while True:
    n = int(input('Insira um valor: '))
    if n == 999:
        break
    else:
        soma += n
        conta += 1
print('='*60)
print(f'Você digitou {conta} números e a soma total é {soma}')