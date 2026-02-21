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
    tipo_busq=int(input("que tipo de busqueda quiere? \n1-por indice\n2-por nombre\n"))
    if tipo_busq==1:
        indice=int(input("que indice tiene el producto que busca? del 1 al numero que escogio en la primera pregunta: "))

        if 1 <= indice <= canti_produc:
            print(f'prudcto: {nombre[indice-1]} \n codigo: {codigo[indice-1]} \n cantidad: {cantidad[indice-1]}')
        else:
            print("no existe ese elemento")
    else:
        nombre_busq=input("digame el nombre el profudcto")

        if nombre_busq in nombre:

            indice=nombre.index(nombre_busq)
            print(f'Producto: {nombre[indice]}')
            print(f'Código: {codigo[indice]}')
            print(f'Cantidad: {cantidad[indice]}')
        else:
            print("no existe ese elemento")

    respuesta=input("desea buscar otro producto?(s/n): ")

respuesta=input("desea  mostrar todo los prouctos?(s/n): ")

if respuesta=='s':
    for nom, cod, cant in zip(nombre, codigo, cantidad):
        print(f'nombre, {nom}\ncodigo: {cod}\ncantidad: {cant}')
