respuesta=input("desea elevar al cuadrado? s/n: ")

while respuesta=="s":
    numero=float(input("digame un numero: "))
    print(f"el numero elevado al cuadrado es: {numero**2}")
    respuesta=input("desea elevar otro numero al cuadrado? s/n: ")