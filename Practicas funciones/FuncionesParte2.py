#1. Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.

""" def calcularAreaRectangulo(base:int, altura:int)->int:
    
    area = (base * altura) / 2
    return area

numero1 = int(input("Ingrese la base: "))
numero2 = int(input("Ingrese la altura: "))

resultado = calcularAreaRectangulo(numero1, numero2)

print(f"El area del triangulo es {resultado}") """


#2. Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

""" def calcularAreaCirculo(radio:int)->int:
    pi = 3.1416
    area = pi * (radio ** 2)
    return area

numero = float(input("Ingrese el radio: "))

resultado = calcularAreaCirculo(numero)

print(f"El area del circulo es {resultado}") """

#3. Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

""" def validarPar(num):
    if num % 2 == 0:
        print(f"El numero {num} es par")
    else:
        print(f"El numero {num} es impar")    

numero = int(input("Ingrese un numero: "))

validarPar(numero) """


#4. Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

""" def validarPar(num):
    flag = True
    if num % 2 == 0:
        flag = True
    else:
        flag = False 
    return flag  

numero = int(input("Ingrese un numero: "))
resultado = validarPar(numero)
print(resultado) """


#5. Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

""" def encontrarMaximo(numero1:int,numero2:int,numero3:int)->int:
    maximo = numero1
    if numero2 > maximo:
        maximo = numero2
    if numero3 > maximo:
        maximo = numero3
    return maximo

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
resultado = encontrarMaximo(num1,num2,num3)

print(resultado) """

#6. Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

""" def calcularPotencia(base:int, exponente:int):
    resultado = base ** exponente
    return resultado

num1 = int(input("Ingrese la base: "))
num2 = int(input("Ingrese el exponente: "))

print(calcularPotencia(num1,num2)) """


#7. Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

""" def buscarPrimo(num):
    contador = 0
    flag = True
    for i in range(1, num + 1):
        if num % i == 0:
            contador += 1
    if contador != 2:
        flag = False
    return flag


numero = int(input("Ingresá un número: "))
print(buscarPrimo(numero)) """


#8. Crear una función que (utilizando la función del punto 11 de la guía de For), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados.

""" def ver_primos(num:int)->int:
    cant_primos = 0

    for i in range(1, num + 1):
        contador = 0
        for j in range(1, i + 1):
            if i % j == 0:
                contador += 1
        if contador == 2:
            print(i)
            cant_primos += 1

    return cant_primos

numero = int(input("Ingrese un número: "))
resultado = ver_primos(numero)

print(f"\n Se encontraron {resultado} números primos.") """

#9. Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.

""" def imprimir_tabla(num, inicio=1, fin=10)->int:

    for i in range(inicio, fin + 1):
        multiplicacion = num * i
        print(multiplicacion)

numero = int(input("Ingrese un numero: "))

imprimir_tabla(numero) """

#10. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

""" def solicitar_entero()->int:
    numero = int(input("Ingrese un numero entero: "))
    return numero """

#11. Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

""" def solicitar_flotante()->float:
    numero = float(input("Ingrese un numero flotante: "))
    return numero """

#12. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.

""" def solicitar_string()->str:
    cadena = str(input("Ingrese una cadena de texto: "))
    return cadena """


#13. Especializar las funciones del punto 10, 11, 12 para hacerlas reutilizables. Agregar validaciones.
