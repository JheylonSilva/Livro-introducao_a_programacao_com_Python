a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
print('---Escolha a operação desejada---')
print('1 para soma')
print('2 para subtração')
print('3 para multiplicação')
print('4 para divisão')

tipo = input('Qual operação você deseja realizar? ')

if tipo == '1':
    operacao = a + b
    print(f"O resultado da operação é {operacao}")

elif tipo == '2':
    operacao = a - b
    print(f"O resultado da operação é {operacao}")

elif tipo == '3':
    operacao = a * b
    print(f"O resultado da operação é {operacao}")

elif tipo == '4':
    operacao = a / b
    print(f"O resultado da operação é {operacao}")
else:
    print('erro: Operação inválida')