from estudiantes import *
from funciones import *

def main ():

    while True:

        print("------------MENU-------------------------")
        print("1-Listar los alumnos por orden ascendente de apellido")
        print("2-Obtener el promedio de notas para cada estudiante")
        print("3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa de “Ingenieria en Informatica” ")
        print("4-Obtener un promedio de edad de los estudiantes")
        print("5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y apellido")
        print("6-Listar nombre y apellido de los alumnos que forman el grupo “Club de Informática” con sus respectivos promedios")
        print("7-Listar legajo, nombre, apellido y programas que cursan los alumnos más jóvenes.")
        print("8-Salir")

        opcion = input("Ingrese una opcion: ")
        match opcion:
            case "1":
                ordenar_alumnos_apellido_ascendente(estudiantes)
            case "2":
                promedio_notas_c_estudiante(estudiantes)
            case "3":
                estudiantes_ing_informatica(estudiantes)
            case "4":
                obtener_promedio(estudiantes)
            case "5":
                alumno_mayor_promedio_notas(estudiantes)
            case "6":
                print("-6")
            case "7":
                print("7")
            case "8":
                print("Salir")
                break
            case _:
                print("Opcion invalida.")
    


main()