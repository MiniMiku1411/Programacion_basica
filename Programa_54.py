nombres = ["Carlos", "Ana", "Luis", "Maria", "Pedro"]
ahorros = [500, 1500000, 800, 250000, 2000000]

for nombre, ahorro in zip(nombres, ahorros):

    if ahorro < 1000:
        print(f"{nombre} no tendrás para tu futuro\n")

    elif ahorro > 1000000:
        print(f"{nombre} ya merito te retiras\n")

    else:
        print(f"{nombre} vas bien, sigue ahorrando\n")