lista=[]
respuesta=input("desea ingresar un dato?(s/n): ")

while respuesta=='s':
    dato=float(input("digame su numero a intgresar?: "))
    lista.append(dato)
    respuesta=input("desea ingresar otro dato?(s/n): ")

lista.sort()

print(lista)
