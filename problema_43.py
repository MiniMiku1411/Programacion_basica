bono=float(input("cantidad a abonar?: "))

while bono<100000:
    bono_extra=float(input("cantidad a abonar?: "))
    if bono_extra<0:
        print("cantidad no valida")
    else:
        bono=bono+bono_extra
        
