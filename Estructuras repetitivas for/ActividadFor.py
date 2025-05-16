#1-----------------------------------------------------------------

'''
for i in range(1,10):
    print(i)

'''

#2-----------------------------------------------------------------

'''

for i in range(10,0,-1):
    print(i)

'''
#3 Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

""" numero = int(input("Ingrese un numero: "))

for i in range(numero + 1):
    print(i)
 """
#4 Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:
# 5 x 0 = 0
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15 


""" numero = int(input("Ingresa un numero: "))

for i in range(numero):
    print(numero, "x", i, "=", (numero * i) ) """


5# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

""" acumulador = 0
promedio = 0

for i in range(10):
    numero = int(input("ingrese un numero: "))
    if numero == 0:
        break
    else:
        
        acumulador += numero
        promedio = int(acumulador / (i+1))

print(f"\n Suma: {acumulador}")
print(f"\n Promedio: {promedio}") """



#6 Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)

""" for i in range(1, 11):
    if i % 3 == 0:
        print(i) """

#7 Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
 
""" for i in range(1,51):
    if i % 2 == 0:
        print(i) """

#8 Realizar un programa que permita mostrar una pirámide de números.

""" for i in range(5):
    for j in range(i):
        print(j+1, end="")
    print() """

#9 Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

""" numero = int(input("Ingrese un numero: "))

for i in range(1,numero):
    if numero % i == 0:
        print(i) """

#10 Ingresar un número. Determinar si el número es primo o no.

""" numero = int(input("Ingresá un número: "))
contador = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        contador += 1

if contador == 2:
    print("El número es primo.")
else:
    print("El número no es primo.") """

11# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

""" cant_primos = 0

numero = int(input("Ingrese un número: "))

for i in range(1, numero + 1):
    contador = 0
    for j in range(1, i + 1):
        if i % j == 0:
            contador += 1
    if contador == 2:
        print(i)
        cant_primos += 1

print(f"\n Se encontraron {cant_primos} números primos.") """
