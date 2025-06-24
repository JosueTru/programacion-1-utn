jugadores = [
       {"nombre": "Ana", "edad": 43, "puntos":[10,12,14]},  
       {"nombre": "Juan", "edad": 32, "puntos":[12,10,11]},  
       {"nombre": "Pedro", "edad": 28, "puntos":[9,15,11]},
       {"nombre": "Sol", "edad": 31, "puntos":[11,8,15]}
]


#buscar el de menor edad y mostrar su nombre

""" edad_minima = jugadores[0]["edad"]
datos_menor = []
for i in range(len(jugadores)):
    if jugadores[i]["edad"] < edad_minima:
        edad_minima = jugadores[i]["edad"]
        datos_menor = jugadores[i]


print(edad_minima)
print(datos_menor) """



#ACUMULAR LOS PUNTOS DE CADA JUGADOR


for jugador in jugadores:
    acumulador = 0
    for i in range(len(jugador["puntos"])):
        acumulador += jugador["puntos"][i]

    print(f"{jugador["nombre"]} tiene un total de {acumulador} puntos")
