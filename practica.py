""" tablero = [[0,0,1,0,0],
           [0,1,0,1,0],
           [1,0,0,1,0],
           [0,0,1,0,1],
           [0,0,0,0,1]]


def verificar_coordenadas(tablero:list, x:int, y:int)->bool:
    mensaje = False

    if tablero[x][y] == 1:
        mensaje = True
    return mensaje



seguir = "s"
while seguir == "s":
    fila = int(input("Ingrese una fila: "))
    while fila < 0 or fila > 4:
        fila = int(input("Ingrese una fila valida (0-4): "))
    columna = int(input("Ingrese una columna: "))
    while columna < 0 or columna > 4:
        columna = int(input("Ingrese una columna valida (0-4): "))

    resultado = verificar_coordenadas(tablero, fila, columna)

    if resultado == True:
        print("Hundidoo")
    else:
        print("Aguaaa")        

    seguir = input("¿Quieres seguir jugando? (s/n): ")

 """
import random
lista = [2,5,6,2,4]

for i in range(2):

    

    random.shuffle(lista)



    numero = lista.pop()

    print(lista)

    print(numero)