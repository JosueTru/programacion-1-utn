def es_primo(n, divisor):
    if n < 2:
        return False
    if divisor == 0:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return es_primo(n, divisor - 1)

# Solicitar número al usuario
numero = int(input("Ingrese un número: "))

if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")