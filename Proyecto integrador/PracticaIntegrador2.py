""" 
1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
inclusive.
2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
3-Porcentaje de jugadores de categoría "experto".
4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite”.
 """

encuestas = 10
cant_jugadores_elite = 0
menor_edad = 0
nombre_menor = ""
categoria_menor = ""
cant_expertos = 0
cant_avanzado = 0
promedio_expertos = 0
contador_elite: 0
promedio_final = 0

saquePlano = 0
saqueLiftado = 0
saqueCortado = 0

for i in range(encuestas):

    nombre = input("Ingrese su nombre: ")

    edad = int(input("Ingrese su edad: "))
    while edad < 15 or edad > 50:
        edad = int(input("Ingrese una edad mayor a 15: "))

    cant_puntos = int(input("Ingrese cantidad de puntos (0-60): "))
    while cant_puntos < 0 or cant_puntos > 60:
        cant_puntos = int(input("Ingrese una cantidad valida: "))



    cant_part_ganados = int(input("Ingrese cantidad de partidos ganados (0-35): "))
    while cant_part_ganados < 0 or cant_part_ganados > 35:
        cant_part_ganados = int(input("Ingrese una cantidad de partidos ganados valida: "))

    tipo_de_saque = input("Ingrese tipo de saque (plano, liftado, cortado): ")
    while tipo_de_saque != "plano" and tipo_de_saque != "liftado" and tipo_de_saque != "cortado":
        tipo_de_saque = input("Ingrese un tipo de saque valido: ")

    categoria = input("Ingrese categoria (elite, experto, avanzado)")
    while categoria != "elite" and categoria != "experto" and categoria != "avanzado":
        categoria = input("Ingrese una categoria valida; ")

    if categoria == "elite" and tipo_de_saque == "plano" and (edad > 18 and edad < 50):
        cant_jugadores_elite += 1
    

    if menor_edad == 0:
        menor_edad = edad
    elif edad < menor_edad:
        menor_edad = edad
        nombre_menor = nombre
        categoria_menor = categoria
    
    if categoria == "experto":
        cant_expertos += 1
        promedio_expertos = (cant_expertos / encuestas) * 100

    if categoria == "avanzado":
        cant_avanzado += edad
        promedio_final = cant_avanzado / encuestas 
    
    if categoria == "elite":
        if tipo_de_saque == "plano":
            saquePlano +=1
        elif tipo_de_saque == "liftado":
            saqueLiftado += 1
        else:
            saqueCortado += 1

if saquePlano >= saqueLiftado and saquePlano >= saqueCortado:
    saque_mas_usado = "plano"
elif saqueLiftado >= saqueCortado:
    saque_mas_usado = "liftado"
else:
    saque_mas_usado = "cortado"
        
   


print("La cantidad de jugadores elite con tipo de saque “plano”, cuya edad esté entre 19 y 25 años: ",cant_jugadores_elite)

print(nombre_menor,"de la ategoria",categoria_menor, "es el/la jugador/a de menor edad con más de 50 puntos")

print(f"El promedio de expertos es del {promedio_expertos}%")

print(f"{promedio_final} es el promedio de edad de los jugadores cuya categoría es “avanzado”")

print(f"El tipo de saque más usado por jugadores 'elite' fue: {saque_mas_usado}")


