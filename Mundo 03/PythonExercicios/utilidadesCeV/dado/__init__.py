def leia_dinheiro(resp):
    res = ''
    while True:
        try:
            res = float(input(resp).replace(',', '.'))
        except ValueError:
            print(f'\033[31mERRO! \"{res}\" é um preço inválido!\033[m')
        else:
            break
    return res


#Resolução da aula
def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO! \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)



