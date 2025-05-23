def alta_producto(lista):
    nuevo_producto = []
    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-4): "))
    
    if lista[fila][columna] == "vacio":
        producto = input("Ingrese un nuevo producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        nuevo_producto = [producto, cantidad]
        lista[fila][columna] = nuevo_producto
        print(lista)
    else:
        print("---------------------------------")
        print("Ya hay un producto en este lugar ")
        print("---------------------------------")


def baja_producto(lista):
    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-4): "))
    if lista[fila][columna] != "vacio":
        lista[fila][columna] = "vacio"
        print(lista)
    else:
        print("No existe objeto")


def modifiar_producto(lista):
    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-4): "))
    if lista[fila][columna] != "vacio":
        fila = int(input("Ingrese nuevo nombre del producto: "))
        columna = int(input("Ingrese cantidad: "))
        lista[fila][columna] = [fila,columna]
        print(lista)




""" resultado = alta_producto(tabla,0,0)

print(resultado) """

