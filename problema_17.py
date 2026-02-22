precio_venta = float(input("Ingresa el precio de venta por pieza: "))
cantidad_vendida = int(input("Ingresa la cantidad vendida: "))
costo_fijo = float(input("Ingresa el costo fijo: "))
costo_variable = float(input("Ingresa el costo variable por pieza: "))

ingresos = precio_venta * cantidad_vendida
costo_total = costo_fijo + (costo_variable * cantidad_vendida)
beneficio = ingresos - costo_total

print(f"Ingresos totales: ${ingresos:.2f}")
print(f"Costo total: ${costo_total:.2f}")
print(f"Beneficio total: ${beneficio:.2f}")
