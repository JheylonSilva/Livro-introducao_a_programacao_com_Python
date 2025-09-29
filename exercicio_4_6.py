pc_1 = 0.50
pc_2 = 0.45
distancia = int(input("Distância a percorrer: "))
if distancia < 200:
    preco = distancia * pc_1
    print(
        f"A distância percorrida foi de {distancia}km e o valor a pagar é de R${preco:5.2f}"
    )
else:
    preco = distancia * pc_2
    print(
        f"A distância percorreda foi de {distancia}km e o valor a pagar é de R${preco:5.2f}"
    )
