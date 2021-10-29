from time import sleep
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
sleep(1)
if media < 5.0:
    print('\n\033[1;31mREPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('\n\033[1;33mRECUPERAÇÃO')
else:
    print('\n\033[1;32mAPROVADO')