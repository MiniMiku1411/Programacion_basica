nom=input("digame su nombre: ")
num_boleta=input("diga su numero de boleta: ")
total=0
for i in range(5):
    calif=float(input("digame su calificacion numero "+str(i+1)+": "))
    total=calif + total
print("\nHola", nom, "con boleta", num_boleta, "el promedio de sus calificaciones es: ", total/5)