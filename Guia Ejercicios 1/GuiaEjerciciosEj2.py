#Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
#adolescente (entre 13 y 17 años) o niño (menor a 13 años).

edad = int(input("ingrese su edad: "))

if edad < 13:
    print("Es menor")
elif edad > 13 and edad < 17:
    print("Es adolecente")
else:
    print("Es mayor")