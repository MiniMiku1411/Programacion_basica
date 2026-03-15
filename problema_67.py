def ordena_creciente(lista):
    lista.sort()
    return lista

def ordena_decreciente(lista):
    lista.sort(reverse=True)
    return lista

def elimina_indice(lista, indice):
    return lista.pop(indice)

def elimina_dato(lista, dato):
    lista.remove(dato)
    return lista

def estadisticas(lista):
    promedio = sum(lista) / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    return promedio, maximo, minimo


numeros = [5,8,2,9,1]

print("Lista original:", numeros)

print("Orden creciente:", ordena_creciente(numeros.copy()))
print("Orden decreciente:", ordena_decreciente(numeros.copy()))

print("Elemento eliminado por índice:", elimina_indice(numeros.copy(),2))
print("Lista eliminando dato:", elimina_dato(numeros.copy(),8))

prom, maxi, mini = estadisticas(numeros)
print("Promedio:", prom)
print("Máximo:", maxi)
print("Mínimo:", mini)