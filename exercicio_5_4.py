fim = int(input('Digite o último npumero a imprimir: '))
x = 0
while x <= fim:
    if x % 2 == 1: #O resto da divisão de x por 2 é igual a zero
        print(x)
    x += 1
