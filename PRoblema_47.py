materias=int(input("cunatas materias desea ingrear: "))
i=0

while  i<materias:
    materia=input(f'como se llama la materia {i+1}: ' )

    calif_num=int(input("cuantas calificaciones tiene esta materia: "))
    j=0
    calificaciones=[]
    while j<calif_num:
        califacacion=float(input(f'cual es su calificacion {j+1}: '))
        calificaciones.append(califacacion)
        j+=1
    suma=sum(calificaciones)

    print(f'tu califacion de {materia} es {suma/calif_num}')
    i+=1
