nombre=input("digame su nombre: ")
vol=float(input("digame el volumen de sus ventas: "))

if vol<1000:
    print(f"{nombre} esta despedido")
elif vol>=1000 and vol<4999:
     print(f"{nombre} esta en periodo de prueba")
elif vol>=5000 and vol<9999.99:
    print(f"{nombre} tiene un bonus del 5%")
elif vol>=10000:
    print(f"{nombre} tiene un bonus del 10%")