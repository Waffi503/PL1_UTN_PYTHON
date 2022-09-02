from data_stark import lista_heroes
# Analizar detenidamente el set de datos
# Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
# Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
# Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
# Calcular e informar cual es el superhéroe más y menos pesado.
# Ordenar el código implementando una función para cada uno de los valores informados.
# Construir un menú que permita elegir qué dato obtener

# 2
def imprimir_heroes(lista_heroes):
    for heroe in lista_heroes:
        print('HEROE : {}'.format(heroe["nombre"]))

#3
def imprimir_heroes_con_altura(lista_heroes):
    for heroe in lista_heroes:
        print('HEROE : {} || ALTURA: {} '.format(heroe["nombre"],heroe["altura"]))

#6
def imprimir_altura_promedio(lista_heroes):

    cantidad_heroes = len(lista_heroes)
    total_altura = 0

    for heroe in lista_heroes:
        altura = float(heroe["altura"])
        total_altura += altura

    altura_promedio = total_altura / cantidad_heroes

    print('LA ALTURA PROMEDIO ES {}'.format(altura_promedio))

#7
def imprimir_altura(lista_heroes,type):

    lista_heroes[0]["altura"] = float(lista_heroes[0]["altura"])

    heroe_mas_alto = lista_heroes[0]
    heroe_mas_bajo = lista_heroes[0]

    for heroe in lista_heroes:
        heroe["altura"] = float(heroe["altura"])

        if( heroe["altura"] > heroe_mas_alto["altura"] ):
            heroe_mas_alto = heroe

        if( heroe["altura"]  < heroe_mas_bajo["altura"] ):
            heroe_mas_bajo = heroe

    if type == "max":
        return print('HEROE MAS ALTO ES {} CON {} '.format(heroe_mas_alto["nombre"],heroe_mas_alto["altura"])) 
    elif type == "min":
        return print('HEROE MAS BAJO ES {} CON {} '.format(heroe_mas_bajo["nombre"],heroe_mas_bajo["altura"]))
    elif type == "ambos":
        return print('EL HEROE MAS ALTO SU IDENTIDAD ES {}, Y EL MAS BAJO SU IDENTIDAD ES {}'.format( heroe_mas_alto["identidad"], heroe_mas_bajo["identidad"] ))


#7
def imprimir_mas_menos_pesado(lista_heroes):

    lista_heroes[0]["peso"] = float(lista_heroes[0]["peso"])

    heroe_mas_pesado = lista_heroes[0]
    heroe_menos_pesado = lista_heroes[0]

    for heroe in lista_heroes:

        heroe["peso"] = float(heroe["peso"])

        if( heroe_mas_pesado["peso"] < heroe["peso"] ):
            heroe_mas_pesado = heroe

        if( heroe_menos_pesado["peso"] > heroe["peso"] ):
            heroe_menos_pesado = heroe
    
    print('EL HEROE MAS PESADO ES {} CON UN PESO DE {} , Y EL HEROE MENOS PESADO ES {} CON UN PESO DE {}'.format(  heroe_mas_pesado["nombre"], heroe_mas_pesado["peso"],  heroe_menos_pesado["nombre"], heroe_menos_pesado["peso"] ))

while True:
    print('Ingrese el numero que necesite')
    print('-1 para salir')
    print('-2 para imprimir los nombres')
    print('-3 para imprimir los nombres y la altura')
    print('-4 para imprimir el heroe mas alto')
    print('-5 para imprimir el heroe mas bajo')
    print('-6 para imprimir la altura promedio')
    print('-7 para imprimir el nombre asociado del hero mas alto y mas bajo')
    print('-8 para imprimir el personaje mas pesado y menos pesado')

    respuesta = input('\n\n> ')

    if respuesta == "1":
        break
    elif respuesta == "2":
        imprimir_heroes(lista_heroes)
    elif respuesta == "3":
        imprimir_heroes_con_altura(lista_heroes)
    elif respuesta == "4":
        imprimir_altura(lista_heroes,"max")
    elif respuesta == "5":
        imprimir_altura(lista_heroes,"min")
    elif respuesta == "6":
        imprimir_altura_promedio(lista_heroes)
    elif respuesta == "7":
        imprimir_altura(lista_heroes,"ambos")
    elif respuesta == "8":
        imprimir_mas_menos_pesado(lista_heroes)


    print('')
