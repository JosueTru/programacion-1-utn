#Ejercicio 1: Dadas las siguientes listas:
#Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
#Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
#Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente.

""" def ordenar_nombre_lista_asc(nombres, edades):
    for i in range(len(nombres)-1):
        for j in range(i+1,len(nombres)):
            if nombres[i] > nombres[j]:
                aux_nombre = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux_nombre
            
                aux_edades = edades[i]
                edades[i] = edades[j]
                edades[j] = aux_edades    

ordenar_nombre_lista_asc(Nombres,Edades)
print(Nombres)
print(Edades)
 """


#Ejercicio 2: Dadas las siguientes listas:
#Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos","Base de Datos", "Ergonomia", "Naturaleza"]
#Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
#Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera descendente.


""" def ordenar_listas_nombre_puntos(nombres, puntos):
    for i in range(len(nombres)-1):
        for j in range(i+1, len(nombres)):
            if nombres[i] > nombres[j]:
                aux_nombres = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux_nombres



                aux_puntos = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = aux_puntos

            elif nombres[i] == nombres[j] and puntos[i] < puntos[j]:
                # Si los nombres son iguales, ordenar por puntos descendente
                aux_puntos = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = aux_puntos    


ordenar_listas_nombre_puntos(Nombres, Puntos)

print(Nombres)
print(Puntos) """


#Ejercicio 3: Dadas las siguientes listas:
#Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
#Apellidos = ["Sosa", "Gutierrez", "Alsina", "Martinez", "Sosa", "Ramirez", "Perez", "Lopez", "Arregui", "Mitre", "Andrade", "Loza", "Antares", "Roca", "Perez"]
#Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
#Desarrollar una función que realice el ordenamiento de las listas por apellido de
#manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera
#ascendente, si el nombre también es el mismo, debe ordenar por nota de manera
#descendente.

""" def ordenar_apellido_nombre_asce_nota_desc(Estudiantes, Apellidos, Nota):
    for i in range(len(Apellidos)-1):
        for j in range(i+1, len(Apellidos)):
            if Apellidos[i] > Apellidos[j]:
                aux_apellidos = Apellidos[i]
                Apellidos[i] = Apellidos[j]
                Apellidos[j] = aux_apellidos

                aux_estudiantes = Estudiantes[i]
                Estudiantes[i] = Estudiantes[j]
                Estudiantes[j] = aux_estudiantes

                aux_nota = Nota[i]
                Nota[i] = Nota[j]
                Nota[j] = aux_nota

            elif Apellidos[i] == Apellidos[j] and Estudiantes[i] > Estudiantes[j]:
                aux_estudiantes = Estudiantes[i]
                Estudiantes[i] = Estudiantes[j]
                Estudiantes[j] = aux_estudiantes

            elif Apellidos[i] == Apellidos[j] and Estudiantes[i] == Estudiantes[j] and Nota[i] < Nota[j]:
                aux_nota = Nota[i]
                Nota[i] = Nota[j]
                Nota[j] = aux_nota
            

  

ordenar_apellido_nombre_asce_nota_desc(Estudiantes,Apellidos,Nota)

print(Estudiantes)
print(Apellidos)
print(Nota) """



