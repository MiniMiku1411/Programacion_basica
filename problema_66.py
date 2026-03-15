calificaciones=[["alex","juan","manuel","alberto"],[89,39,14,100]]

def reprobados(lista):
    reprobados=[]

    for i in range(len(lista[0])):
        if lista[1][i]<70:
            reprobados.append(lista[0][i])

    return reprobados

print(reprobados(calificaciones))