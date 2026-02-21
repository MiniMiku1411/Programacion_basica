canti_produc=int(input("cuantos productos ingresara?: "))

nombre=[]
codigo=[]
cantidad=[]

i=0

while i<canti_produc:
    nom=input(f'digame el nombre del producto {i+1}: ')
    nombre.append(nom)
        
    cod=input(f'digame el codigo del producto {i+1}: ')
    codigo.append(cod)

    cant=input(f'digame la cantida que hay del producto {i+1}: ')
    cantidad.append(cant)

    i+=1

respuesta=input("desea buscar un producto especifico?(s/n): ")

while respuesta=='s':

    indice=int(input("que indice tiene el producto que busca? del 1 al numero que escogio en la primera pregunta: "))
    print(f'prudcto: {nombre[indice-1]} \n codigo: {codigo[indice-1]} \n cantidad: {cantidad[indice-1]}')

    respuesta=input("desea buscar otro producto?(s/n): ")

respuesta=input("desea  mostrar todo los prouctos?(s/n): ")

if respuesta=='s':
    for nom, cod, cant in zip(nombre, codigo, cantidad):
        print("nombre:", nom)
        print("codigo:", cod)
        print("cantidad:", cant)

