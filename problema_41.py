contra=input("digame su contraseña: ")
contra_confirmacion=input("confirme su contraseña: ")
while contra!=contra_confirmacion:
    print("Las contraseñas no coinciden. Inténtalo de nuevo.")
    contra_confirmacion=input("confirme su contraseña: ")


