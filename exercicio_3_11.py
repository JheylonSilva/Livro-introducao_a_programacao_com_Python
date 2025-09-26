preco = int(input("Informe o preço da mercadoria: "))
desconto = int(input("Informe o percentual de desconto: "))
vlr_desconto = preco * (desconto / 100)
vlr_a_pagar = preco - vlr_desconto
print(f"O valor do desconto é de R${vlr_desconto:5.2f}")
print(f"O preço a pagar será de R${vlr_a_pagar:5.2f}")