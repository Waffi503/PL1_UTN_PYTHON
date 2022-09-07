from textwrap import indent
from data_stark import lista_heroes

def obtener_primero_genero(genero):
    index = 0
    for heroe in lista_heroes:
        if(heroe["genero"] == genero ):
            return heroe
        
    return {}

# A - B
def imprimir_heroes_genero(genero):
    for heroe in lista_heroes:
        if(heroe["genero"] == genero):
            print(heroe["nombre"])

# C - D - E - F - G - H
def imprimir_altura(lista_heroes, genero, type):

    primer_heroe = obtener_primero_genero(genero)

    if(primer_heroe == {}):
        return print("No se encontro ningun personaje de ese genero")
  
    primer_heroe["altura"] = float(primer_heroe["altura"])
    heroe_mas_alto = primer_heroe
    heroe_mas_bajo = primer_heroe
    
    cantidad = 0
    altura_total = 0 

    for heroe in lista_heroes:
        heroe["altura"] = float(heroe["altura"])

        if( heroe["altura"] > heroe_mas_alto["altura"] and heroe["genero"] == genero ):
            heroe_mas_alto = heroe

        if( heroe["altura"]  < heroe_mas_bajo["altura"] and heroe["genero"] == genero ):
            heroe_mas_bajo = heroe

        if( heroe["genero"] == genero ):
            cantidad += 1
            altura_total += heroe["altura"]

    if type == "max":
        return print('HEROE MAS ALTO {0} ES {1} CON {2} '.format(genero, heroe_mas_alto["nombre"], heroe_mas_alto["altura"])) 
    elif type == "min":
        return print('HEROE MAS BAJO {0} ES {1} CON {2} '.format(genero, heroe_mas_bajo["nombre"],heroe_mas_bajo["altura"]))
    elif type == "promedio":
        altura_promedio = altura_total / cantidad
        return print('LA ALTURA PROMEDIO DEL GENERO {0} es {1} '.format(genero, altura_promedio))
    # elif type == "ambos":
    #     return print('EL HEROE MAS ALTO SU IDENTIDAD ES {}, Y EL MAS BAJO SU IDENTIDAD ES {}'.format( heroe_mas_alto["identidad"], heroe_mas_bajo["identidad"] ))


def cantidad_tipo(tipo):

    diccionario = {}

    for heroe in lista_heroes:
        try:
            diccionario[heroe[tipo].lower()] += 1
        except:
            diccionario[heroe[tipo].lower()] = 1

    print(diccionario)

def imprimir_tipo_agrupado(tipo):

    colores = []

    for heroe in lista_heroes:
        if(heroe[tipo] == ""):
            heroe[tipo] = "No tiene"

        if (not any(heroe[tipo].lower() in color.lower() for color in colores)):
            colores.append(heroe[tipo])

    color_agrupado = {}

    for heroe in lista_heroes:
        for color in colores:
            if( heroe[tipo].lower() == color.lower() ):
                try:
                    color_agrupado[color].append(heroe)
                except:
                    color_agrupado[color] = [heroe]

    print(color_agrupado)
        


while True:

    print('Ingrese el numero que necesite')
    print('-1 para salir')
    print('-2 para imprimir los nombres del genero M')
    print('-3 para imprimir los nombres del genero F')
    print('-4 para imprimir el heroe mas alto M')
    print('-5 para imprimir el heroe mas alto F')
    print('-6 para imprimir el heroe mas bajo M')
    print('-7 para imprimir el heroe mas bajo F')
    print('-8 para imprimir el promedio de altura del genero M')
    print('-9 para imprimir el promedio de altura del genero F')
    print('-10 para listar todos los heroes agrupados por color de ojo')
    print('-11 para listar todos los heroes agrupados por color de pelo')
    print('-12 para listar todos los heroes agrupados por inteligencia')

    respuesta = input('\n\n> ')

    if respuesta == "1":
        break
    elif respuesta == "2":
        imprimir_heroes_genero("M")
    elif respuesta == "3":
        imprimir_heroes_genero("F")
    elif respuesta == "4":
        imprimir_altura(lista_heroes, "M", "max")
    elif respuesta == "5":
        imprimir_altura(lista_heroes, "F", "max")
    elif respuesta == "6":
        imprimir_altura(lista_heroes, "M", "min")
    elif respuesta == "7":
        imprimir_altura(lista_heroes, "F", "min")
    elif respuesta == "8":
        imprimir_altura(lista_heroes, "M", "promedio")
    elif respuesta == "9":
        imprimir_altura(lista_heroes, "F", "promedio")
    elif respuesta == "10":
        imprimir_tipo_agrupado("color_ojos")
    elif respuesta == "11":
        imprimir_tipo_agrupado("color_pelo")
    elif respuesta == "12":
        imprimir_tipo_agrupado("inteligencia")


    print('')