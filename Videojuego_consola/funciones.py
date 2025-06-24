import random
from preguntas import *


def pedir_nombre():
    nombre = input("Ingrese su nombre: ")
    return nombre


# Valida las opciones para seguir o no
def validar_opcion(opcion:str)->str:

    #Inicia el bucle while para que solo acepte s / n
    while opcion != "s" and opcion != "n":
        opcion = input("Error, Ingrese una opcion valida (s/n): ").lower()

    return opcion
###

def ingresar_opcion(texto:str)->str:
    opcion = input(texto).lower()
    opcion_validada = validar_opcion(opcion)

    return opcion_validada


###
def mezclar_nueva_lista(preguntas:list)->list:
    preguntas_copia = preguntas.copy()
    random.shuffle(preguntas_copia)
    return preguntas_copia



def sacar_pregunta(preguntas:list)->dict:
    pregunta_elegida = preguntas.pop()

    return pregunta_elegida

#   Mostrar la pregunta y opciones
def mostrar_pregunta(diccionario:dict):
    print("-" * 40)
    print(f"{diccionario["pregunta"]}")
    print(f"a) {diccionario["respuesta_a"]}")
    print(f"b) {diccionario["respuesta_b"]}")
    print(f"c) {diccionario["respuesta_c"]}")


# Valida las respuestas
def validar_respuesta(respuesta:str)->str:
    while respuesta != "a" and respuesta != "b" and respuesta != "c":
        respuesta = input("Error, Ingrese una respuesta valida (a - b - c): ").lower()

    return respuesta
     

#ahora empieza la funcionalidad

def mover(diccionario:dict, respuesta:str, posicion:int, tablero:list)->int:

    respuesta_correcta = diccionario["respuesta_correcta"]


    operacion = calcular_direccion_base(respuesta, respuesta_correcta)
    posicion += operacion

    
    posicion = calcular_direccion_tablero(posicion, tablero, operacion)


    print(f"Tu posicion actual es {posicion} !")

    

    return posicion






def calcular_direccion_base(respuesta_validada:str,respuesta_correcta:str)->int:
    calculo = 0
    if respuesta_validada == respuesta_correcta:
        calculo = 1
        print("-CORRECTO-")
    else:
        calculo = -1
        print("-INCORRECTO-")

    return calculo


def calcular_direccion_tablero(posicion:int,tablero:list, operacion:int)->int:
    salto_adicional = tablero[posicion]
    posicion += salto_adicional * operacion
    return posicion




def verificar_estado_juego(posicion:int, ultima_casilla:int)->str:
    estado = "continua"

    if posicion >= ultima_casilla:
        print("-" * 40)
        print("FELICIDADES GANASTE! ")
        print("-" * 40)

        estado = "gano"
    elif posicion <= 0:
        print("-" * 40)
        print("Perdiste. volve a intentarlo")
        print("-" * 40)

    
        estado = "perdio"

    return estado
    

###
def guardar_datos(nombre_jugador: str, posicion: int):
    with open("puntaje.csv", "a") as puntajes:
        puntajes.write(f"{nombre_jugador} - {posicion} puntos.\n")
###





