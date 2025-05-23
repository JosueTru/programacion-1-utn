#Ejercicio 1: El almacén de barrio nos pide un programa para almacenar, ordenar y
#controlar stock de su mercadería por día.
#Comienza el día con la siguiente disposición en su góndola:
#Cada celda (fila/columna) muestra la ubicación de cada producto, ejemplo: en (1,2)
#se guardan las botellas, etc.
#Armar la lista de Productos con nombre, cantidad y ubicación (fila, columna)

from biblioteca import *

tabla = [["vacio",["botellas", 3], "vacio", ["frascos", 5], "vacio"],
         ["vacio","vacio",["fideos", 2], "vacio", "vacio"],
         ["vacio","vacio","vacio",["leche", 6],"vacio"]]

while True:

    print("1-Alta de productos (producto nuevo)")
    print("2-Baja de productos (producto existente)")
    print("3-Modificar productos (cantidad, ubicación)")
    print("4-Listar productos")
    print("5-Lista de productos ordenado por nombre")
    print("6-Salir")

    opcion = input("Ingrese una opcion: ")

    match opcion:
        case "1":
            alta_producto(tabla)
        case "2":
            baja_producto(tabla)
        case "3":
            modifiar_producto(tabla)
        case "4":
            print("opcion 1")
        case "6":
            print("Cerrando el programa")
            break
