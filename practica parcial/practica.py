mapa = [
 [0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0] ]


def verificar_tesoro(mapa: list, x: int, y: int) -> int:

    # Solucion al entregralo
    """ x_tesoro = 1
    y_tesoro = 3

    distancia = x - x_tesoro + y - y_tesoro """

    # Solucion completa (Actualizado despues de entregarlo)
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 1:
                x_tesoro = i
                y_tesoro = j

                calculo_x = x - x_tesoro
                calculo_y = y - y_tesoro

                if calculo_x < 0:
                    calculo_x *= -1
                elif calculo_y < 0:
                    calculo_y *= -1

                distancia = calculo_x + calculo_y
    #------------------------------------------------------

    # Convertir la distancia a un numero positivo
    """ if distancia < 0:
        distancia *= (-1) """

    return distancia

opcion = "s"
while opcion == "s":

    fila = int(input("Ingrese una fila (0-4): "))
    while fila < 0 or fila > 4:
        fila = int(input("Ingrese una fila dentro del rango valido (0-4): "))

    columna = int(input("Ingrese una columna (0-4): "))
    while columna < 0 or columna > 4:
        columna = int(input("Ingrese una columna dentro del rango valido (0-4): "))


    resultado = verificar_tesoro(mapa, fila, columna)

    if resultado == 0:
        print("¡Encontraste el tesoro!")
        opcion = "n"
    else:

        print(f"Fallaste. El tesoro está a {resultado} casilleros de distancia.")
        opcion = input("Queres seguir intentando? (s/n): ")

        