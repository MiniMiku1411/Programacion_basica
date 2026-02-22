edad=int(input("digame su edad: "))


if edad<0 or edad>120:
        print("edad invalida")
else:
    if edad<10:
        print("usted es un niño")
    elif edad<18:
        print("usted es un adolescente")
    elif edad<29:
        print("usted es un joven")
    elif edad<59:
        print("usted es un adulto")
    else:
        print("usted es un adulto mayor")