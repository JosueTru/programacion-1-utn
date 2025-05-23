#Realizar una función recursiva que calcule la suma de los primeros números naturales:

""" def sumar_naturales(numero: int) -> int:
    if numero == 0:
        resultado = 0
    else:
        resultado = numero + sumar_naturales(numero - 1)
    return resultado
print(sumar_naturales(4)) """


#2. Realizar una función recursiva que calcule la potencia de un número:

""" def calcular_potencia(base, exponente):
    if exponente == 0:
        resultado = 1
    else:
        resultado = base * calcular_potencia(base, exponente - 1)

    return resultado

print(calcular_potencia(5, 3)) """


#3. Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

""" def sumar_digitos(numero: int) -> int:
    if numero < 10:
        resultado = numero
    else:
        resultado = (numero % 10) + sumar_digitos(numero // 10)
        print(numero % 10)
        print(numero // 10)
    return resultado


print(sumar_digitos(262)) """

