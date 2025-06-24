from funciones import *
from preguntas import *
from datos import *

""" posicion = 15
tablero = [0,1,0,0,0,3,0,0,0,0,0,1,0,0,2,1,1,0,0,0,1,0,0,2,0,0,0,1,0,0,0]

posicion_ganador = len(tablero) - 1
posicion_perdedor = 0 """


def main(preguntas:list, posicion:int, tablero:list):

    # Pide nombre y señal para empezar, tambien hace la copia de la lista de preguntas y la mezcla
    nombre_jugador = pedir_nombre()

    preguntas_copia = copiar_lista(preguntas)
    preguntas_copia = mezclar(preguntas_copia)

    señal = ingresar_opcion("Quiere iniciar el juego? (s/n): ")

    #Inicia el bucle segun la señal del jugador
    while señal == "s":

        #Cuando la lista de preguntas termina, finaliza el juego
        if not preguntas_copia:
            print("\nSe acabaron las preguntas.")
            print(f"Tu puntaje final es: {posicion}")
            break
        
        #Elegimos la pregunta
        pregunta_elegida = sacar_pregunta(preguntas_copia)

        #Imprimimos las pregunta y opciones
        mostrar_pregunta(pregunta_elegida)

        # Pide y valida la respuesta del jugador
        respuesta = input("Ingrese su respuesta (a - b - c): ").lower()
        respuesta = validar_respuesta(respuesta)


        #Posicion final del jugador ya calculado
        posicion = mover(pregunta_elegida, respuesta, posicion, tablero)

        #Corta el bucle si el jugador gana o pierde
        estado = verificar_estado_juego(posicion, posicion_ganador)
        if estado != "continua":
            break

        # Esto sucede al final de cada accion
        señal = ingresar_opcion("Quiere seguir jugando? (s/n): ")

    print(f"\nTermino en la posicion {posicion}")
    print("Finalizando el juego, hasta luego")
    guardar_datos(nombre_jugador, posicion)
    
    
main(preguntas, posicion, tablero)
        

