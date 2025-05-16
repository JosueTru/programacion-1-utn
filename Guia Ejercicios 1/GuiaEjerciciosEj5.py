#Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
#por cada estadía como base, se pide el ingreso de una estación del
#año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
#Plata/Córdoba) para vacacionar para poder calcular el precio final:
#-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
#descuento del 10% Mar del Plata tiene un descuento del 20%
#-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
#un aumento del 10% Mar del Plata tiene un aumento del 20%
#-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
#aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
#precio sin descuento.
#Validar el ingreso de datos

precio = 15000

estacion = input("Ingrese una estación del año (Invierno/Verano/Otoño/Primavera): ")
while estacion != "invierno" and estacion != "verano" and estacion != "primavera" and estacion != "otoño":
    estacion = input("Ingrese una estación válida: ")

localidad = input("Ingrese una localidad(Bariloche/Cataratas/Mar del Plata/Córdoba) ")
while localidad != "bariloche" and localidad != "cataratas" and localidad != "mar del plata" and localidad != "cordoba":
    localidad = input("Ingrese una localidad valida: ")

if estacion == "invierno":
    if localidad == "bariloche":
        precio = precio + (precio * 0.2)
    elif localidad == "cataratas" or localidad == "cordoba":
        precio = precio - (precio * 0,1)
    elif localidad == "mar del plata":
        precio = precio - (precio * 0.2)
elif estacion == "verano":
    if localidad == "bariloche":
        precio = precio - (precio * 0,2)
    elif localidad == "cataratas" or localidad == "cordoba":
        precio = precio + (precio * 0.1)
    elif localidad == "mar del plata":
        precio = precio + (precio * 0.2)
elif estacion == "otoño" or estacion == "primavera":
    if localidad == "bariloche" or localidad == "cataratas" or localidad == "mar del plata":
        precio = precio + (precio * 0.1)
    elif localidad == "cordoba":
        precio = precio
        
    

print(precio)
