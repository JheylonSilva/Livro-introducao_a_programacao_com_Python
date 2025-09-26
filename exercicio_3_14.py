custo_diaria = 60
custo_km = 0.15

km_percorrido = int(input("Informe o km percorrido: "))
qtd_dias = int(input("O carro foi alugado por quantos dias: "))

vlr_pagar = (km_percorrido * custo_km) + (qtd_dias * custo_diaria)
print(f"O carro foi alugado por {qtd_dias} dias e o total a pagar será de R${vlr_pagar:5.2f}")