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

# funcion que se encarga de obtener la opcion del usuario y usa la validacion ya vista
def ingresar_opcion(texto:str)->str:
    opcion = input(texto).lower()
    opcion_validada = validar_opcion(opcion)

    return opcion_validada


# Copia la lista de preguntas para luego usarla y modificarla
def copiar_lista(preguntas:list)->list:
    preguntas_copia = preguntas.copy()

    """ random.shuffle(preguntas_copia) """

    return preguntas_copia

def mezclar(preguntas_copia:list):
    random.shuffle(preguntas_copia)
    return preguntas_copia



# Saca el ultimo elemento de la lista de diccionarios y la guarda en una variable para retornar
def sacar_pregunta(preguntas:list)->dict:
    pregunta_elegida = preguntas.pop()

    return pregunta_elegida

#   Toma el diccionario sacado para mostrar la pregunta y opciones
def mostrar_pregunta(diccionario:dict):
    print("-" * 40)
    print(f"{diccionario["pregunta"]}")
    print(f"a) {diccionario["respuesta_a"]}")
    print(f"b) {diccionario["respuesta_b"]}")
    print(f"c) {diccionario["respuesta_c"]}")


# Valida las respuestas de la pregunta dadas por el jugador
def validar_respuesta(respuesta:str)->str:
    while respuesta != "a" and respuesta != "b" and respuesta != "c":
        respuesta = input("Error, Ingrese una respuesta valida (a - b - c): ").lower()

    return respuesta
     

#ahora empieza la funcionalidad del juego

def mover(diccionario:dict, respuesta:str, posicion:int, tablero:list)->int:

    #Toma la respuesta correcta del dict elegido
    respuesta_correcta = diccionario["respuesta_correcta"]

    #Calcula la direccion y saltos
    operacion = calcular_direccion_base(respuesta, respuesta_correcta)
    posicion += operacion

    posicion = calcular_direccion_tablero(posicion, tablero, operacion)


    print(f"Tu posicion actual es {posicion} !")

    return posicion





# Calccula la direccion a la que se mueve el jugador
def calcular_direccion_base(respuesta:str,respuesta_correcta:str)->int:
    calculo = 0
    if respuesta == respuesta_correcta:
        calculo = 1
        print("-CORRECTO-")
    else:
        calculo = -1
        print("-INCORRECTO-")

    #retorna si avanza o retrocede
    return calculo

# Aca calcula la suma con la posicion que cae en el tablero usando el positivo o negativo del calculo base
def calcular_direccion_tablero(posicion:int,tablero:list, operacion:int)->int:
    salto_adicional = tablero[posicion]
    posicion += salto_adicional * operacion
    return posicion


###########

def verificar_estado_juego(posicion:int, ultima_casilla:int)->str:
    estado = "continua"

    # Muestra y calcula si el jugador gano o perdio
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
    

# Guarda los datos en un archivo puntaje.csv
def guardar_datos(nombre_jugador: str, posicion: int):
    with open("puntaje.csv", "a") as puntajes:
        puntajes.write(f"{nombre_jugador} || {posicion} puntos.\n")
###########





