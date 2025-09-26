salario = int(input("Informe o salário: "))
aumento = int(input("Informe o percentual de aumento: "))
vlr_aumento = salario * (aumento / 100)
novo_salario = vlr_aumento + salario
print(f"O valor do aumento é {vlr_aumento}")
print(f"O valor do novo salário é R${novo_salario:5.2f}")