from time import process_time_ns

##1
def validar_convertir_float( dato ):
    """
        Valida si se puede convertir en float
        dato: puede ser de cualquier tipo de dato
        
        retorno: un valor Booleano True si se puede convertir False si no se puede convertir
    """
    if( not type(dato) == int and  not type(dato) == float ):
        try:
            float(dato)
            return True
        except:
            return False
    return False


def stark_normalizar_datos( lista : list = [] ):
    """
    Recorre la lista y convierte al tipo de dato correcto las keys (solo con las keys que representan datos numéricos)

    lista: debe ser una lista de diccionarios 

    retorno: si se  ingresa una lista vacia retorna una lista vacia si no la lista normalizada 
    """
    i = 0 

    if(lista == [] or type(lista) != list ):
        print("Error: Lista de héroes vacía")
        return {}

    for element in lista:
        for subelement in element:
            if(validar_convertir_float(element[subelement])):
                element[subelement] = float(element[subelement])
                i+=1
    if(i > 0):
        print("Datos normalizados")

    return lista


def obtener_nombre( heroe : dict = {} ):
    """
    Obtiene el nombre del heroe que le pasen por parametro

    heroe: tiene que ser un diccionario con la key "nombre"

    retorno: retorna una variable msg con  un mensaje personalizado
    """

    if( type(heroe) != dict or heroe == {}):
        msg = "No ingreso el tipo de dato correcto"
        return msg
    try:
        msg = "Nombre: {0}".format(heroe["nombre"])
        return msg
    except:
        msg = "No ingreso ningun heroe"
        return msg


def imprimir_dato( dato : str = "" ):
    """
    imprime el dato que se le pase por parametro

    dato: tiene que ser un dato tipo string
    """
    if(type(dato) == str):
        print(dato)


def stark_imprimir_nombres_heroes( lista : list = [] ):
    """
    recorre la lista que le pasen por parametro y imprime el nombre de los heroes usando funciones anteriormente declaradas

    lista: una lista de heroe

    retorno: retorna solo si el dato ingresado no es una lista o esta vacia 
    """
    
    if(type(lista) != list or lista == []):
        return -1
    
    for element in lista:
        imprimir_dato(obtener_nombre(element))

# 2 del desafio #00
def obtener_nombre_y_dato( heroe : dict = {}, dato : str = "" ):
    """
    obtiene el nombre y un dato especificado por parametro

    heroe: tiene que ser un diccionario de un heroe
    dato: es el dato solicitado del heroe :)

    retorno: retorna un msg con los datos especificados
    """

    if( type(heroe) != dict or heroe == {} ):
        msg = "No ingreso un heroe"
        return msg

    if( type(dato) != str or dato == "" ):
        msg = "No ingreso una key"
        return msg

    msg = "Nombre: {0} | {1}: {2}".format(heroe["nombre"], dato, heroe[dato])
    return msg

def stark_imprimir_nombres_alturas( lista : list = [] ):
    """
    recorre la lista de heroe y imprime el nombre y la altura de cada uno

    lista: tiene que ser una lista de heroes

    retorno: solo retorna un -1 si lo que se ingresa no es una lista o esta vacia
    """

    if(type(lista) != list or lista == []):
        return -1

    for element in lista:
        print(obtener_nombre_y_dato(element,"altura"))

#3
def calcular_max( lista : list = [], dato : str = ""  ):
    """
    recorre la lista de heroe y imprime el nombre el max de el dato que pidas

    lista: tiene que ser una lista de heroes
    dato: tiene que ser una key de el heroe tiene que ser string

    retorno: el heroe max
    """
    heroe_max = lista[0]

    for element in lista:

        if(element[dato] > heroe_max[dato]):
            heroe_max = element
    
    return heroe_max

def calcular_min( lista : list = [], dato : str = ""  ):
    """
    recorre la lista de heroe y imprime el nombre el min de el dato que pidas

    lista: tiene que ser una lista de heroes
    dato: tiene que ser una key de el heroe tiene que ser string

    retorno: el heroe min
    """

    heroe_min = lista[0]

    for element in lista:
        if(element[dato] < heroe_min[dato]):
            heroe_min = element
    
    return heroe_min


def calcular_max_min_dato( lista : list = [], tipo : str = "", dato : str = ""  ):
    """
    recorre la lista de heroe y imprime el nombre el max o min de el dato que pidas

    lista: tiene que ser una lista de heroes
    tipo: tiene que ser maximo o minimo
    dato: tiene que ser una key de el heroe tiene que ser string

    retorno: el heroe min o el max
    """
    if( tipo == "maximo"):
        return calcular_max(lista,dato)
    elif( tipo == "minimo"):
        return calcular_min(lista,dato)


def stark_calcular_imprimir_heroe ( lista : list = [], tipo : str = "", dato : str = ""  ):
    """
    recorre la lista de heroe y imprime el nombre el max o min de el dato que pidas

    lista: tiene que ser una lista de heroes
    tipo: tiene que ser maximo o minimo
    dato: tiene que ser una key de el heroe tiene que ser string

    retorno: el heroe min o el max
    """
    heroe = calcular_max_min_dato(lista,tipo,dato)
    msg = obtener_nombre_y_dato(heroe,dato)
    imprimir_dato("{0} {1}: {2}".format(tipo,dato,msg ))


def sumar_dato_heroe( lista : list = [], dato : str = "" ):

    acumulado = 0
    for element in lista:
        if( type(element) == dict and element != {} ):
            acumulado += element[dato]

    return acumulado

def dividir( dividiendo : int = 0, divisor : int = 0):

    resultado = 0
    if(divisor == 0):
        return resultado

    resultado = dividiendo / divisor
    return resultado

def calcular_promedio( lista : list = [], dato : str = "" ):

    total = sumar_dato_heroe(lista,dato)
    cantidad_datos = len(lista)
    promedio = dividir(total,cantidad_datos)

    return promedio

def stark_calcular_imprimir_promedio_altura( lista : list = [] ):

    if(type(lista) != list or lista == []):
        return -1

    imprimir_dato(calcular_promedio(lista,"altura"))

def stark_menu_principal():



