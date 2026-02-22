nombre_evento = input("Ingresa el nombre del evento: ")
fecha = input("Ingresa la fecha del evento: ")
asistentes = int(input("Ingresa el número de asistentes: "))

agua_total = asistentes * 1.5
carne_total = asistentes * 350              
salsa_total = agua_total * 0.25       

print("Evento:", nombre_evento)
print("Fecha:", fecha)
print("Asistentes:", asistentes)
print(f"Agua de jamaica necesaria: {agua_total} litros")
print(f"Carne necesaria: {carne_total} gramos")
print(f"Salsa necesaria: {salsa_total} litros")
