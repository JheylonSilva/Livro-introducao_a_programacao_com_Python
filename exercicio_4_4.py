#salário >1250 aumento de 10%
#salário <=1250 aumento de 15%

salario = float(input("Informe o salário: "))
base = 1250
pc_1 = 0.10
pc_2 = 0.15

if salario > base:
    aumento = salario * pc_1
else:
    aumento = salario * pc_2

print(aumento)
