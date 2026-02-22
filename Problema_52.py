productos = ["Lapiz", "Cuaderno", "Borrador", "Regla", "Pluma"]
precios = [10, 25, 8, 15, 12]
ventas = [50, 30, 40, 20, 60]

for productos, precios, ventas in zip(productos,precios,ventas):
    print(f'nombre:{productos} \nprecio:{precios} \nventas:{ventas}\n')