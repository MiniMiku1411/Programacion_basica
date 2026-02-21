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
    tipo_busq=int(input("que tipo de busqueda quiere\n1-por indice \n2-por nombre del producto"))

respuesta=input("desea  mostrar todo los prouctos?(s/n): ")

if respuesta=='s':
    for nom, cod, cant in zip(nombre, codigo, cantidad):
        print("nombre:", nom)
        print("codigo:", cod)
        print("cantidad:", cant)