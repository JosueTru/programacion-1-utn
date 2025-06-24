from estudiantes import *

def ordenar_alumnos_apellido_ascendente(estudiantes):
    
    for i in range(len(estudiantes)-1):
        for j in range(i + 1, len(estudiantes)):

            if estudiantes[i]["apellido"] > estudiantes[j]["apellido"]:
                aux = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux
            
            elif estudiantes[i]["apellido"] == estudiantes[j]["apellido"] and estudiantes[i]["nombre"] > estudiantes[j]["nombre"] :
                aux_nom = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux_nom

    for e_estu in estudiantes:    
        print(e_estu["apellido"], e_estu["nombre"])   


def promedio_notas_c_estudiante(estudiantes:list):
   

    for e_estudiantes in estudiantes:
        suma = 0
        for i in range(len(e_estudiantes["notas"])):
            suma += e_estudiantes["notas"][i]

        
        promedio = suma / len(e_estudiantes["notas"])
        print(f"El estudiantes {e_estudiantes["nombre"]} tiene un promedio de {promedio}")



def estudiantes_ing_informatica(estudiantes):


    for e_estudiantes in estudiantes:
        if e_estudiantes["programa"]["nombre"] == "Ingenieria en Informatica":
            print(f"legajo: {e_estudiantes["legajo"]} | nombre y apellido: {e_estudiantes["nombre"]} {e_estudiantes["apellido"]} | edad: {e_estudiantes["edad"]}")


def obtener_promedio(estudiantes):
    total = 0
    for e_estudiantes in estudiantes:
        total += e_estudiantes["edad"]
    
    promedio = total / len(estudiantes)

    print(f"El promedio de edad de los estudiantes es {promedio}")



def alumno_mayor_promedio_notas(estudiantes):
    
    mayor_promedio = 0
    mejor_estudiante = {}

    for estudiante in estudiantes:
        notas = estudiante["notas"]

        if len(notas) > 0:
            total = 0

            for nota in notas:
                total += nota
            promedio = total / len(notas)
            print(total)
            if promedio > mayor_promedio:
                mayor_promedio = promedio
                mejor_estudiante = estudiante

    if mejor_estudiante:
        print("El alumno con mayor promedio es:")
        print(mejor_estudiante["nombre"], mejor_estudiante["apellido"], f"con un promedio de {mayor_promedio:.2f}")
    else:
        print("No se encontró ningún estudiante con notas.")

    


alumno_mayor_promedio_notas(estudiantes)


    

