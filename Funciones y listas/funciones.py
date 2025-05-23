#1-Importar listas
#2-Listar los datos de los usuarios de México
#3-Listar los nombre, mail y teléfono de los usuarios de Brasil
#4-Listar los datos del/los usuario/s más joven/es
#5-Obtener un promedio de edad de los usuarios
#6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
#7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
#8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.

from listas_personas import *

#2-Listar los datos de los usuarios de México


def listar_datos_mexico(nombres, telefonos, mails, address, postalZip, region, country, edades):
    posicion = []
    for i in range(len(country)):
        if country[i] == 'Mexico':
            posicion.append(i)


    print(f"{'Nombre':<15} | {'Teléfono':<15} | {'Mail':<20} | {'Address':<20} | {'postalZip':<15} | {'Región':<15} | {'Country':<15} | {'Edad':<15}")

    for i in range(len(posicion)):
        indice = posicion[i]

        print(f"{nombres[indice]:<15} | {telefonos[indice]:<15} | {mails[indice]:<20} | {address[indice]:<20} | {postalZip[indice]:<15} | {region[indice]:<15} | {country[indice]:<15} | {edades[indice]:<15}")


#3-Listar los nombre, mail y teléfono de los usuarios de Brasil

def listar_nombre_mail_telefono_brazil(nombres,mails,telefonos):
    posicion = []
    for i in range(len(country)):
        if country[i] == 'Brazil':
            posicion.append(i)

    for i in range(len(posicion)):
        indice = posicion[i]

        print(f"{nombres[indice]:<15} | {mails[indice]:<25} | {telefonos[indice]:<15}")
    

#4-Listar los datos del/los usuario/s más joven/es

def usuarios_mas_jovenes(nombres, telefonos, mails, address, postalZip, region, country, edades):
    edad_maxima = edades[0]
    posiciones_edad = []

    for i in range(len(edades)):
        if edades[i] < edad_maxima:
            edad_maxima = edades[i]

        if edad_maxima == edades[i]:
            posiciones_edad.append(i)

    for i in range(len(posiciones_edad)):
        indice = posiciones_edad[i]
        print(f"{nombres[indice]:<15} | {telefonos[indice]:<15} | {mails[indice]:<20} | {address[indice]:<20} | {postalZip[indice]:<15} | {region[indice]:<15} | {country[indice]:<15} | {edades[indice]:<15}")


#5-Obtener un promedio de edad de los usuarios

def obtener_promedio_edad(edades):
    suma_total_edades = 0
    for i in range(len(edades)):
        suma_total_edades += edades[i]

    promedio = suma_total_edades / len(edades)
    return promedio
        
        
#6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
        

def listar_usuarios_mas_edad_brazil(edades, country):
    edad_maxima = edades[0]
    posiciones_edad = []
    posiciones_country = []

    for i in range(len(country)):
        if country[i] == 'Brazil':
            posiciones_country.append(i)

    for i in range(len(posiciones_country)):
        indice = posiciones_country[i]
        if edades[indice] > edad_maxima:
            edad_maxima = edades[indice]
            if edad_maxima == edades[indice]:
                indice_final = indice
    
    print(f"{nombres[indice_final]:<15} | {telefonos[indice_final]:<15} | {mails[indice_final]:<20} | {address[indice_final]:<20} | {postalZip[indice_final]:<15} | {region[indice_final]:<15} | {country[indice_final]:<15} | {edades[indice_final]:<15}")





#7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000


def encontrar_indice_mexico(country):
    posicion = []
    for i in range(len(country)):
        if country[i] == 'Mexico':
            posicion.append(i)
    return posicion

def encontrar_indice_brazil(country):
    posicion = []
    for i in range(len(country)):
        if country[i] == 'Brazil':
            posicion.append(i)
    return posicion
            


def listar_datos_mexico_brazil_cp8000(nombres, telefonos, mails, address, postalZip, region, country, edades):
    indice_mexico = encontrar_indice_mexico(country)
    indice_brazil = encontrar_indice_brazil(country)
    indice_mexi_brazuca = indice_mexico + indice_brazil
    postalZip_filtrado = []

    
    for i in range(len(indice_mexi_brazuca)):
        index = indice_mexi_brazuca[i]
        if postalZip[index] > 8000:
            postalZip_filtrado.append(index)

        
        
    for i in range(len(postalZip_filtrado)):
        indice_final = postalZip_filtrado[i]
        
        print(f"{nombres[indice_final]:<15} | {telefonos[indice_final]:<15} | {mails[indice_final]:<20} | {address[indice_final]:<35} | {postalZip[indice_final]:<15} | {region[indice_final]:<15} | {country[indice_final]:<15} | {edades[indice_final]:<15}")



 #8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.

           

    

        





