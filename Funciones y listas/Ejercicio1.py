#Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los
#guarde en una lista y la retorne. El programa principal debe invocar a la función y
#mostrar por pantalla el retorno.



""" def pedir_nombres():
    lista = []
    for i in range(2):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        lista.append(nombre)
    return lista


nombres = pedir_nombres()

print("Lista de nombres ingresados:")

for i in range(len(nombres)):
    print(nombres[i], end=' ') """



#Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida
#posición y número a guardar al usuario, lo guarde en una lista en la posición
#solicitada aleatoriamente y la retorne. El programa principal debe invocar a la
#función y mostrar por pantalla el retorno.


""" def inicializar_lista():
    lista_nueva = [0] * 10
    posicion = int(input("Ingrese la posicion que quiere modificar: "))
    while posicion < 0 or posicion > len(lista_nueva):
        posicion = int(input("Ingrese una posicion valida: "))
    numero = int(input("Ingrese el numero que quiere ingresar: "))
    lista_nueva[posicion] = numero
    return lista_nueva

lista_final = inicializar_lista()

print(lista_final) """


#Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango
#especificado, validar los números solicitados dentro de ese rango, guardar en una
#lista y retornarla. El programa principal debe invocar a la función y mostrar por
#pantalla el retorno.

""" def validar_lista():
    seguir = "s"
    lista = []
    while seguir == "s":
        numeros = int(input("Ingrese los numeros que quiera agregar: "))
        while numeros < 0 or numeros > 10:
            numeros = int(input("Ingrese un numero valido: "))
        lista.append(numeros)

        if len(lista) < 10:
            seguir = input("¿Desea seguir agregando números? (s/n): ").lower()
        else:
            seguir = "n"
    

    return lista

lista_hecha = validar_lista()

print(lista_hecha) """


#Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números
#y un número especificado. La misma debe buscar el número especificado en la lista
#y retornar “True” si existe.

""" def buscar_numero(lista, numero):
    resultado = False
    for i in range(len(lista)):
        if lista[i] == numero:
            resultado = True

    return resultado

numeros = [2,5,12,7,1]

num = int(input("Ingrese un numero: "))

respuesta = buscar_numero(numeros, num)

print(respuesta)
 """


#Ejercicio 5: Dadas las siguientes listas:
#Desarrollar una función que reciba por parámetro la lista de edades, busque a las
#personas de menor edad (puede ser más de una) y las retorne. El programa
#principal deberá mostrar nombre y edad de los menores.



""" def encontrar_menor(listaEdad):
    edad_minima = listaEdad[0]
    contador = 0

    lista_posiciones = []

    for i in range(len(listaEdad)):
        if listaEdad[i] < edad_minima:
            edad_minima = listaEdad[i]
        
        if edades[i] == edad_minima:
            contador += 1
        
        if edad_minima == listaEdad[i]:
            lista_posiciones.append(i)

    return lista_posiciones





Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]

edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]


posiciones = encontrar_menor(edades)

print(f"se encontrontraron los menores:")
for i in range(len(posiciones)):
    indice = posiciones[i]

    print(Nombres[indice])

print(f"Todos con la edad de {edades[indice]} años") """
    

#Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo
#listas_personas.py. Importar los nombres a una lista. Realizar una función que
#muestre los mismos.


""" from listas_personas import *

def mostrar_listas(lista):
    for i in range(len(lista)):
        print(lista[i], end=", ")



mostrar_listas(nombres) """


#Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de
#compras on-line recientemente lanzado al mercado para ello necesita un programa
#que le permita acceder a los datos relevados.
#Realizar una función con el siguiente Menú de Opciones:

#1-Importar listas
#2-Listar los datos de los usuarios de México
#3-Listar los nombre, mail y teléfono de los usuarios de Brasil
#4-Listar los datos del/los usuario/s más joven/es
#5-Obtener un promedio de edad de los usuarios
#6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
#7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
#8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.

from listas_personas import *
from funciones import *

def menu():

    while True:
        print("\n--- MENÚ ---")
        print("1-Importar listas")
        print("2-Listar los datos de los usuarios de México")
        print("3-Listar los nombre, mail y teléfono de los usuarios de Brasil")
        print("4-Listar los datos del/los usuario/s más joven/es")
        print("5-Obtener un promedio de edad de los usuarios")
        print("6-De los usuarios de Brasil, listar los datos del usuario de mayor edad")
        print("7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000")
        print("8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.")
        print("9-Salir del programa.")

        opcion = input("Ingrese una opcion: ")

    
        match opcion:
            case "1":
                print("mostrar lista")
            case "2":
                listar_datos_mexico(nombres, telefonos, mails, address, postalZip, region, country, edades)
            case "3":
                listar_nombre_mail_telefono_brazil(nombres,mails,telefonos,country)
            case "4":
                usuarios_mas_jovenes(nombres, telefonos, mails, address, postalZip, region, country, edades)
            case "5":
                print(obtener_promedio_edad(edades))
            case "6":
                listar_usuarios_mas_edad_brazil(edades,country)
            case "7":
                listar_datos_mexico_brazil_cp8000(nombres, telefonos, mails, address, postalZip, region, country, edades)
            case "8":
                print("mostrar lista8")
            case "9":
                break
            
        seguir = input("\n¿Desea realizar otra operación? (s/n): ").lower()
        if seguir != "s":
            print("Programa finalizado.")
            break



