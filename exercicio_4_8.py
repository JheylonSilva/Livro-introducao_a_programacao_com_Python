plano = input("Qual é o seu plano de celular? ")
if plano != "falapouco" and plano != "falamuito":
    print("Não conheço este plano")
else:
    if plano == "falapouco":
        minutos_no_plano = 100
        extra = 0.20
        preço = 50
    else:
        minutos_no_plano = 500
        extra = 0.15
        preço = 99

    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Vocẽ vai pagar: ")
    print(f"Preço do plano R${preço:10.2f}")
    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
    print(f"Suplemento     R${suplemento:10.2f}")
    print(f"Total          R${preço + suplemento:10.2f} ")
