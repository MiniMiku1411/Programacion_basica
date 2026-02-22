tipo = input("¿Deseas crear una lista de números o de texto? (n/t): ")

lista = []

if tipo == "n":
    es_numerica = True
elif tipo == "t":
    es_numerica = False
else:
    print("Opción inválida")
    exit()

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar valor")
    print("2. Eliminar por índice")
    print("3. Eliminar por valor")
    print("4. Ordenar lista (modificando original)")
    print("5. Ordenar lista (crear nueva lista)")
    print("6. Buscar elemento y mostrar índices")
    if es_numerica:
        print("7. Mostrar máximo, mínimo, suma y promedio")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        valor = input("Ingresa el valor: ")
        if es_numerica:
            valor = float(valor)
        lista.append(valor)
        print("Valor agregado.")

    elif opcion == "2":
        if len(lista) == 0:
            print("Lista vacía.")
        else:
            indice = int(input("Ingresa el índice a eliminar: "))
            if 0 <= indice < len(lista):
                lista.pop(indice)
                print("Elemento eliminado.")
            else:
                print("Índice inválido.")

    elif opcion == "3":
        valor = input("Ingresa el valor a eliminar: ")
        if es_numerica:
            valor = float(valor)
        if valor in lista:
            lista.remove(valor)
            print("Valor eliminado.")
        else:
            print("Ese valor no existe.")

    elif opcion == "4":
        lista.sort()
        print("Lista ordenada:", lista)

    elif opcion == "5":
        nueva_lista = sorted(lista)
        print("Nueva lista ordenada:", nueva_lista)

    elif opcion == "6":
        valor = input("Ingresa el valor a buscar: ")
        if es_numerica:
            valor = float(valor)
        indices = [i for i, v in enumerate(lista) if v == valor]
        if indices:
            print("Se encontró en los índices:", indices)
        else:
            print("No se encontró el elemento.")

    elif opcion == "7" and es_numerica:
        if len(lista) == 0:
            print("Lista vacía.")
        else:
            print("Máximo:", max(lista))
            print("Mínimo:", min(lista))
            print("Suma:", sum(lista))
            print("Promedio:", sum(lista) / len(lista))

    elif opcion == "0":
        print("Programa terminado.")
        break

    else:
        print("Opción inválida.")