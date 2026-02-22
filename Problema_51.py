nom=[]
asist=[]

cant_perso=int(input("cuantas personas hay de personal: "))

i=0

while i<cant_perso:
    nombre=input(f'nombre del trabajador {i+1}: ')
    nom.append(nombre)
    asistencia=input("el trabajador asistio hoy?\n1-si\n2-no\n")
    asist.append(asistencia)
    i+=1

for nom, asist in zip(nom, asist):
    if int(asist)==1:
        asistencia="si asistio"
    else:
        asistencia="no asistio"

    print(f'{nom} : {asistencia}')