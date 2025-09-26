velocidade = int(input("Informe a velocidade do carro: "))
limite = 80
multa_km = 5


if velocidade > 80:
    calc_multa = (velocidade - limite) * multa_km
    print(f"O limite de {limite}km/h foi ultrapassado e uma multa no valor de R${calc_multa:5.2f} será aplicada!") 