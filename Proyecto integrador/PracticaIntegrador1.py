


cant_gen_masc = 0
cant_total = 0
cant_empleados = 0
edad_mayor = 0
nombre_mayor = ""
tecnologia_mayor = ""
encuestas = 10

for i in range(encuestas):

    nombre = input("Ingrese su nombre: ")

    edad = int(input("Ingrese su edad: "))

    while edad < 18:
        edad = int(input("Error. Ingrese una edad mayor a 18"))

    genero = input("Ingrese su genero(masculino - femenino- otro): ")

    while genero != "masculino" and genero != "femenino" and genero != "otro":
        genero = input("Ingrese un genero valido")

    tecnologia = input("Ingrese tecnologia (IA, RV/RA, IOT): ")

    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input("Ingrese una tecnologia valida")
    


    if genero == "masculino":
        if tecnologia != "RV/RA" and (edad >= 25 and edad <= 50):
            cant_gen_masc += 1

    if tecnologia != "IA":
        if genero != "femenino" and (edad > 33 and edad < 40):
            cant_empleados += 1
    
    if genero == "masculino":
        if nombre_mayor == "" or edad > edad_mayor:
            edad_mayor = edad
            nombre_mayor = nombre
            tecnologia_mayor = tecnologia

        



porcentaje = float((cant_empleados / encuestas) * 100)
    
print("Cantidad de empleados de género masculino que votaron por IOT o IA,cuya edad esté entre 25 y 50 años es: ", cant_gen_masc)
print("Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40 es: ", porcentaje,"%")
print("El empleado", nombre_mayor, "que voto por la tecnologia", tecnologia_mayor, "fue el mayor de los empleados con", edad_mayor, "años de edad")