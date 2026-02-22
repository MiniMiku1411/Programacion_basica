contra=input("digame su contraseña: ")
contra_confirmacion=input("confirme su contraseña: ")
intentos=0
while intentos<3 and contra!=contra_confirmacion:
    intentos=intentos+1
    print("Las contraseñas no coinciden. Inténtalo de nuevo.")
    contra_confirmacion=input("confirme su contraseña: ")

if intentos==3:
    print("cuenta cancelada")