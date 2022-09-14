from data_stark import lista_heroes

def extraer_iniciales( nombre_heroe : int = "" ):
    '''
    extrae la iniciales 
    primero valida si es una string vacia
    segundo remplaza los guines por espacios vacios
    tercero separa los nombres convertiendolo en una lista
    cuarto recorre la lista y mientras que el nombre no sea igual a "the" suma a iniciales la primera letra en mayusculas junto a un "."

    retorno: las iniciales
    '''
    if nombre_heroe == "":
        return 'N/A'

    nombre_heroe = nombre_heroe.replace("-", "")
    lista = nombre_heroe.split()
    iniciales = ""

    for i in lista:
        if(i.lower() != "the"):
            iniciales += i[0].upper() + '.'

    return iniciales

def definir_iniciales_nombre( heroe : dict = {} ):
    '''
    valida que sea un diccionario y que tenga algo en nombre, luego agrega la key iniciales junto a su valor
    
    retorno: true si no hubo problemas, false si hubo problemas
    '''

    if (type(heroe) != dict or len(heroe["nombre"]) == 0):
        return False

    iniciales_heroe = extraer_iniciales(heroe["nombre"])
    heroe["iniciales"] = iniciales_heroe
    return True

def agregar_iniciales_nombre( lista_heroe : list =[]):

    if(type(lista_heroe) != list or len(lista_heroe) == 0):
        return False
    
    for heroe in lista_heroe:
        if(not definir_iniciales_nombre(heroe)):
            return False

    return True

def stark_imprimir_nombres_con_iniciales( lista_heroe : list =[] ):
    '''
    valido la lista, luego imprimo con f"" como lo pide el ejercicio :)
    void function
    '''
    if(type(lista_heroe) == list and len(lista_heroe) > 0):
        agregar_iniciales_nombre(lista_heroe)
        for heroe in lista_heroe:
            print(f'* {heroe["nombre"]} ({heroe["iniciales"]})')



def generar_codigo_heroe(id_heroe : int = 0, genero_heroe : str = ''):
    '''
    valida los parametros, luego genera el codigo del genero osea ("F-" - "M-" - "NB-")
    luego convierte a str la id del heroe, luego rellena de 0 lo que seria la id heroe con la cantidad de 10 - el tamaño del genero code
    
    '''
    codigo_heroe = 'N/A'
    if(type(id_heroe) != int ):
        return codigo_heroe
    if( genero_heroe != 'M' and genero_heroe != 'F' and genero_heroe != 'NB' or genero_heroe == ""):
        return codigo_heroe

    genero_code = f"{genero_heroe}-"
    id_heroe = str(id_heroe)
    id_heroe = id_heroe.zfill(10-len(genero_code))
    codigo_heroe = genero_code + id_heroe
    return codigo_heroe

def agregar_codigo_heroe( heroe : dict = {} ):
    

    
