""" Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los
guarde en una lista y la retorne. El programa principal debe invocar a la función y
mostrar por pantalla el retorno.
 """


def pedir_nombres():
    lista = []
    for i in range(10):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        lista = lista + [nombre]
    return lista


nombres = pedir_nombres()
print("Lista de nombres ingresados:")
print(nombres)