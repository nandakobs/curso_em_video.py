digitados = 0
soma = 0
nums = 0
# digitados = soma = nums = 0  # Assim tds as variaveis recebem o mesmo valor
print('Me diga quantos números você quiser, para parar digite 999')
while nums != 999:
    nums = int(input('Insira um valor: '))
    if nums != 999:
        digitados += 1
        soma += nums
print('{} números foram digitados e a soma deles é {}.'.format(digitados, soma))