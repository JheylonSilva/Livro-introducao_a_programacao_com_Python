dividendo = int(input('Digite o valor que será dividido: '))
divisor = int(input('Digite por quanto será dividido: '))
quociente = 0
x = dividendo

while x >= divisor:
    x = x - divisor
    quociente += 1
    
print(quociente)

   

