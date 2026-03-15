lista1=[1,2,3,4,5]

def cuadrado(list):
    lista2=[]

    for i in list:
        lista2.append(i**2)
    return lista2

print(cuadrado(lista1))