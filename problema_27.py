desicion=int(input("quiere calcular el area o el perimetro del cuadrado? 1 para area, 2 para perimetro: "))

if desicion==1:
    lado=int(input("digame el valor del lado del cuadrado: "))
    print(f"el area del cuadrado es: {lado*lado}")
elif desicion==2:
    lado=int(input("digame el valor del lado del cuadrado: "))
    print(f"el perimetro del cuadrado es: {lado*4}")
else:
    print("opcion no valida")