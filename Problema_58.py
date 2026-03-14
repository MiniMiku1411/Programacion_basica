Lista=[]

def llenado():
    respuesta="s"
    while respuesta=="s":
        Lista.append(float(input("Digame un numero: ")))
        respuesta=input("desea ingresar otro dato?: ")
    print(f'su lista es {Lista}')

llenado()
