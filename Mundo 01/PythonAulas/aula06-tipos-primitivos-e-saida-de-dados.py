# int()    para numeros inteiros
# float()  para numeros reais
# bool()   booleano pra False/True
# str()    string
n = input('Diga algo ai ')
print(n.isnumeric()) #é numero?
print(n.isalpha()) #é letra?
print(n.isalnum()) #é aplhanumerico?
print(n.isupper()) #tá tudo em maiusculo?
n1 = int(input('Digite um numero:'))
print(type(n1)) #type retorna o tipo de class
n2 = int(input('Digite outro numero:'))
soma = n1 + n2
#print('A soma entre', n1, 'e', n2 , 'vale', soma)
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))



