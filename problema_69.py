def verificar(Correo):
    if "@" in Correo:
        return "direccion de correo electronico valida"
    else:
        return "direccion de correo electronico no valido"
    
correo=input("diga su correo: ")

print(verificar(correo))
