from funciones import *
from preguntas import *
from datos import *

""" posicion = 15
tablero = [0,1,0,0,0,3,0,0,0,0,0,1,0,0,2,1,1,0,0,0,1,0,0,2,0,0,0,1,0,0,0]

posicion_ganador = len(tablero) - 1
posicion_perdedor = 0 """


def main(preguntas, posicion, tablero):


    nombre_jugador = pedir_nombre()

    preguntas_copia = mezclar_nueva_lista(preguntas)

    señal = ingresar_opcion("Quiere iniciar el juego? (s/n): ")

    while señal == "s":

        if not preguntas_copia:
            print("Se acabaron las preguntas.")
            print(f"Tu puntaje final es: {posicion}")
            break

        pregunta_elegida = sacar_pregunta(preguntas_copia)


        mostrar_pregunta(pregunta_elegida)


        respuesta = input("Ingrese su respuesta (a - b - c): ").lower()
        respuesta = validar_respuesta(respuesta)



        posicion = mover(pregunta_elegida, respuesta, posicion, tablero)


        estado = verificar_estado_juego(posicion, posicion_ganador)
        if estado != "continua":
            break

        # Esto sucede al final de cada accion
        señal = ingresar_opcion("Quiere seguir jugando? (s/n): ")

    print(f"\nTermino en la posicion {posicion}")
    print("Finalizando el juego, hasta luego")
    guardar_datos(nombre_jugador, posicion)
    
    
main(preguntas, posicion, tablero)
        

