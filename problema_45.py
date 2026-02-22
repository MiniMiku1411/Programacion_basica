def calculadora(num1, num2):
    operacion=input("que operacion desea hacer? 1-suma, 2-resta, 3-multiplicacion o 4-division 5-exponente 6-modulo: ")

    if operacion=="1":
        print(f"el resultado de la suma es: {num1+num2}")
    elif operacion=="2":
        print(f"el resultado de la resta es: {num1-num2}")
    elif operacion=="3":    
        print(f"el resultado de la multiplicacion es: {num1*num2}")
    elif operacion=="4":
        if num2==0:
            print("no se puede dividir entre cero")
        else:
            print(f"el resultado de la division es: {num1/num2}")
    elif operacion=="5":
        print(f"el resultado del exponente es: {num1**num2}")  
    elif operacion=="6":
        if num2==0:
            print("no se puede dividir entre cero")
        else:
            print(f"el resultado del modulo es: {num1%num2}")
    else:
        print("operacion no valida")

respuestas=input("desea hacer una operacion? s/n: ") 
while respuestas=="s":
    num1=float(input("digame el primer numero: "))
    num2=float(input("digame el segundo numero: "))

    calculadora(num1, num2)
    respuestas_2=input("desea hacer otra operacion con estos datos? s/n: ")
    while respuestas_2=="s":
        calculadora(num1, num2)
        respuestas_2=input("desea hacer otra operacion con estos datos?xd s/n: ")
    respuestas=input("desea hacer una operacion nueva? s/n: ") 