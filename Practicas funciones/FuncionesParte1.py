#1 Crear una función que muestre por pantalla el número que recibe como parámetro.

""" def mostrar_numero(num:int): 
    print(num)

numero = int(input("Ingrese un numero; "))

mostrar_numero(numero) """

#2 Crear una función que pida el ingreso de un número y lo retorne.

""" def mostrar_numero(): 
    numero = int(input("ingrese un numero: "))
    return numero

numero_ingresado = mostrar_numero()

print(numero_ingresado) """



#3 Crear una función que permita determinar si un número es par o no. La función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el programa principal realizando la invocación o llamada.


""" def determinarPar (numero:int)->bool:
    resultado = False
    if numero % 2 == 0:
        resultado= True

    return resultado

numero = int(input("Ingrese un numero: "))

if determinarPar(numero):
    print(numero,"es par")
else:
    print(numero,"es impar")
 """
        
#4 Especializar la función del punto 3.1 y 3.2 para que valide el número en un rango determinado pasado por parámetro “desde”-“hasta”.


""" def mostrar_numero(desde, hasta): 
    numero = int(input("ingrese un numero: "))
    while numero < desde or numero > hasta:
        numero = int(input("ingrese un numero dentro del rango asignado"))
    return numero

numero_ingresado = mostrar_numero(10, 15)

print(f"El numero ingresado ({numero_ingresado}) es valido") """


#5 Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la función Restar en sus 4 combinaciones.
# Restar1(int, int)->int:
# Restar2()->int:
# Restar3(int, int):
# Restar4():

""" def restar1(num1:int, num2:int)->int:
    resta = num1 - num2
    return resta

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

print(restar1(numero1, numero2)) """

""" def restar2()->int:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    resta = num1 - num2
    return resta

print(restar2()) """

""" def restar3(num1:int, num2:int):
    resta = num1 - num2
    print(resta)


numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
restar3(numero1, numero2) """

""" def restar4():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    resta = num1 - num2
    print(resta)

restar4()
 """


#6 : Realizar un programa que: asigne a la variable numero1 un valor solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado
# por pantalla. Atención: pueden reutilizarse funciones ya creadas.

def realizarDescuento(num:int)->int:
    descuento = (num / 100) * 5
    resultado = num - descuento
    return resultado

numero1 = int(input("Ingrese un numero: "))
while numero1 < 10 or numero1 > 100:
    numero1 = int(input("Ingrese un numero valido: "))

resultado_final = int(realizarDescuento(numero1))
print(resultado_final)

