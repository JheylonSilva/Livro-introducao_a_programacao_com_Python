valor_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salário: '))
anos_quitacao = int(input("Informe a quantidade de anos para pagar:  "))

meses = anos_quitacao * 12
parcelas = valor_casa / meses
perc_salario = salario * 0.30

if parcelas > perc_salario:
    print("A parcela do financiamento é superior a '30%' do salário")

else:
    print(f'O valor financiado será de R${valor_casa:10.2f}')
    print(f'O valor da parcela será de R${parcelas:10.2f}')


