ingresos=int(input("digame el precio unitario de los productos: "))
cantidad=int(input("digame la cantidad de productos: "))
egresos=int(input("digame el costo de los gastos: "))

ganancia= (ingresos*cantidad)

if ganancia>egresos:
    print(f"estamos en perdidad")
elif ganancia<egresos:
    print(f"estamos en ganancia")
else:
    print(f"estamos en equilibrio")
