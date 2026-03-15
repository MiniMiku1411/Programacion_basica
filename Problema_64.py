def EsMultiplo(num1,num2):
    dato= num1%num2
    if dato==0:
        return f'{num1} es multiplo de {num2}'
    else:
        return f'{num1} no es multiplo de {num2}'
    
n1= float(input("diga su primer numero: "))
n2= float(input("diga su segundo numero: "))

print(EsMultiplo(n1,n2))

    