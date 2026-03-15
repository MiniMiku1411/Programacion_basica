def primo(num):
    dato=num%2

    if dato==0:
        return "el no es primo"
    elif num==2:
        return "el numero es primo"
    else:
        return "el numero es primo"
    
numero=float(input("diga su numero: "))

print(primo(numero))