Cap_ini=input("diame la capital inical: ")
Tas_int=float(input("diame la tasa de interes: "))
Periodos=int(input("diame el numero de periodos: "))

Int_Com=Cap_ini*(1+Tas_int)**Periodos
print(f"el interes compuesto es: {Int_Com}")

respuesta=input("desea calcular otro interes compuesto? s/n: ")
while respuesta=="s":
    Cap_ini=input("diame la capital inical: ")
    Tas_int=float(input("diame la tasa de interes: "))
    Periodos=int(input("diame el numero de periodos: "))

    Int_Com=Cap_ini*(1+Tas_int)**Periodos
    print(f"el interes compuesto es: {Int_Com}")

    respuesta=input("desea calcular otro interes compuesto? s/n: ")