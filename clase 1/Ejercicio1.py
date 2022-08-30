#La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
#El tipo (validar "barbijo", "jabón" o "alcohol")
#El precio: (validar entre 100 y 300)
#La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
#La marca y el Fabricante.

# Se debe informar lo siguiente:
#Del más caro de los barbijos, la cantidad de unidades y el fabricante.
#Del ítem con más unidades, el fabricante.
#Cuántas unidades de jabones hay en total.

from re import A


total_jabones = 0
primer_barbijo = True

for carga in range(5):

    if(carga == 0):
        print('Bievenido al programa, Primera vuelta')
    else:
        print('Vuelta nro: ' + str(carga + 1))

    tipo = input("Ingrese el tipo de producto  \n ")
    while (tipo != 'barbijo' and tipo != 'jabon' and tipo != 'alcohol'  ):
        tipo = input("Ingrese el tipo de producto: 'barbijo' - 'jabon' - 'alcohol'  \n ")
    
    precio = input("ingrese el precio \n")
    precio = float(precio)
    while(precio < 100 or precio >300):
        precio = input("ingrese el precio \n")
        precio = float(precio)

    cantidad = input('ingrese la cantidad de unidades \n')
    cantidad = int(cantidad)
    while(cantidad < 0 or cantidad > 1000):
        cantidad = input('ingrese la cantidad de unidades \n')
        cantidad = int(cantidad)
    
    marca = input('ingrese la marca \n')
    
    fabricante = input('ingrese el fabricante \n')

    if(tipo == 'barbijo' ):
        if(primer_barbijo or barbijo_caro_precio < precio  ):
            barbijo_caro_precio = precio
            barbijo_caro_cantidad = cantidad
            barbijo_caro_fabricante = fabricante
            primer_barbijo = False

    if(carga == 0 or item_mas_unidades_cantidad < cantidad ):
        item_mas_unidades_cantidad = cantidad
        item_mas_unidades_tipo = tipo 
        item_mas_unidades_fabricante = fabricante

    if(tipo == 'jabon'):
        total_jabones += cantidad

print('La cantidad de jabones es: ' + str(total_jabones) )

if( not primer_barbijo):
    print('El barbijo mas caro se vendieron una cantidad de: ' + str(barbijo_caro_cantidad) + ' y el fabricante es: ' + barbijo_caro_fabricante)
else:
    print('No se vendieron barbijos')

print('El item con mas unidades es: ' + item_mas_unidades_tipo + ' y el fabricante es: ' + item_mas_unidades_fabricante )