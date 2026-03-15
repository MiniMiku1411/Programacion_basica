def factorial(num):
    factorial=1
    numero=num
    while num>0:    
        factorial=factorial*num
        num=num-1
    return f'el factorial de {numero} es {factorial}'

respuesta="s"
veces=0

while respuesta=="s":
    numero=float(input("digame su numero: "))
    print(factorial(numero))
    veces=veces+1
    respuesta=input("quiere saber otro numero?s/n: ")

print(f'su total de veces de busqueda fue de {veces}')