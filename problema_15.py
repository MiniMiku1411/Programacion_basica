nom_prod=input("diga el nombre del producto: ")
precio_prod=input("diga el precio del producto: ")

prod_iva= float(precio_prod)*0.19+float(precio_prod)
print("el producto ", nom_prod, " tiene un precio de: ", precio_prod, " sin iva, con iva es: ", prod_iva)