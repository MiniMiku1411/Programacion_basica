capital_inicial = float(input("Ingresa el capital inicial: "))
tasa_interes = float(input("Ingresa la tasa de interés anual (%): "))
periodos = int(input("Ingresa el número de periodos: "))

tasa = tasa_interes / 100

capital_simple = capital_inicial * (1 + tasa * periodos)

capital_compuesto = capital_inicial * (1 + tasa) ** periodos

print(f"Capital final con interés simple: ${capital_simple:.2f}")
print(f"Capital final con interés compuesto: ${capital_compuesto:.2f}")
