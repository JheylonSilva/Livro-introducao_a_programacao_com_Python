dias = int(input("Dias: "))
horas = int(input("horas: "))
minutos = int(input("minutos: "))
segundos = int(input("segundos: "))

# 1 minuto tem 60 segundos
# 1 hora tem 3600 (60 * 60) segundos
# 1 dia tem 24 horas e 86.400 segundos
total = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print(f"O total convertido em segundos é igual a {total} segundos.")