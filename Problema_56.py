lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
cantidad=len(lista)
i=1

while i<=10:
    new_dat=lista[cantidad-1]
    lista.append(new_dat+1)
    cantidad+=1
    i+=1

for elemnto in lista:
    print(elemnto)


