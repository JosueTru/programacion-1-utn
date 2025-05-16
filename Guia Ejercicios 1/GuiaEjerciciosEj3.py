#Ingresar 5 números enteros, distintos de cero.
#Informar:
#a. Cantidad de pares e impares.
#b. El menor número ingresado.
#c. De los pares el mayor número ingresado.
#d. Suma de los positivos.
#e. Producto de los negativos

pares = 0
impares = 0
par_mayor = 0
flag = True
suma_pos = 0
producto_neg = 1
numero_menor = 0
total = 0


for i in range(5):
    numero = int(input("Ingreses un numero: "))

    if numero == 0:
        print("Datos invalidos")
    else:
        if (numero % 2) == 0:
            pares += 1
            if flag == True:
                par_mayor = numero
                flag = False
            elif numero > par_mayor:
                par_mayor = numero
        else:
            impares += 1

    if i == 0:
        numero_menor = numero
    elif numero < numero_menor:
        numero_menor = numero

    if numero > 0:
        suma_pos += numero
    else:
        producto_neg *= numero

    total += numero
            
print("La cantidad de numeros pares es de: ", pares)
print("La cantidad de numeros impares es de: ", impares)
print("El numero menor es: ", numero_menor)
print("El numero par mayor es: ", par_mayor)
print("La suma de los positivos es: ", suma_pos)
print("El producto de los negativos es: ", producto_neg)
print("La suma de todos los numeros ingresados es de: ",total)
