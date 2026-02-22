calif=int(input("digame su calificacion del 1 al 10: "))

if calif<0 or calif>10:
    print("la calificacion no puede ser negativa ni mayor a 10")
elif  calif<6:
    print("reprobado")
elif calif>6 and calif<10:
    print("regular")
else:
    print("sobresaliente")