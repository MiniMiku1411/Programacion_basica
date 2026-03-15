def promedio(prom1,prom2,prom3):
    total=(prom1+prom2+prom3)/3

    if total<7:
        return f'te vas a extras con {total}'
    else:
        return f'pasas con {total}'

calif_1=float(input("digame su primera calificacion: "))
calif_2=float(input("digame su segunda calificacion: "))
calif_3=float(input("digame su tercera calificacion: "))

calificacion=promedio(calif_1,calif_2,calif_3)
print(calificacion)