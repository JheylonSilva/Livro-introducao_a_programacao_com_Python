consumo = int(input('Qual a quantidade de kWh consumida: '))
print('----Informe o tipo de instalação----')
print('-----R para residências-----')
print('-----I para indústrias-----')
print('-----C para comércios-----')

tipo = input('Qual o tipo de instalação: ')

if tipo == 'r':
    if consumo <= 500:
        total = consumo * 0.40
        print(f'O valor a pagar será de R${total:10.2f}')
    elif consumo > 500:
        total = consumo * 0.65
        print(f'O valor a pagar será de R${total:10.2f}')

if tipo == 'c':
    if consumo <= 1000:
        total = consumo * 0.55
        print(f'O valor a pagar será de R${total:10.2f}')
    elif consumo > 1000:
        total = consumo * 0.60
        print(f'O valor a pagar será de R${total:10.2f}')

elif tipo == 'i':
    if consumo <= 5000:
        total = consumo * 0.55
        print(f'O valor a pagar será de R${total:10.2f}')
    elif consumo > 5000:
        total = consumo * 0.60
        print(f'O valor a pagar será de R${total:10.2f}')   

else:
    if tipo != 'r' and tipo !='i' and tipo != 'c':
        print('erro: a opção selecionada é inválidada!!')