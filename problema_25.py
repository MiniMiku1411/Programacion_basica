x1=int(input("inrese la cordenada x1: "))
y1=int(input("inrese la cordenada y1: "))
x2=int(input("inrese la cordenada x2: "))
y2=int(input("inrese la cordenada y2: "))

if x2-x1==0:
    print("la pendiente es indefinida")
    exit()
pendiente=(y2-y1)/(x2-x1)
b=y1 - pendiente*x1
if pendiente==1:
    print(f"La ecuacion de la recta es: y= x + {b}")
else:
    print(f"La ecuacion de la recta es: y={pendiente}x + {b}")