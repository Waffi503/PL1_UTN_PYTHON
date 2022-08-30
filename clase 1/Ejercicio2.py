# La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para la cocina de Industrias Wayne. 
# Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
# preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
    # 1 PESO: (entre 10 y 100 kilos)
    # 2 PRECIO POR KILO: (mayor a 0 [cero]).
    # 3 TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
# Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto. o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.
    # A El importe total a pagar, BRUTO sin descuento.
    # B El importe total a pagar con descuento (Solo si corresponde).
    # C Informar el tipo de alimento más caro.
    # D El promedio de precio por kilo en total.

from ast import While


continuar = input("")
print("Bievenido al programa")

while (continuar == "si"):

    peso = input("Ingrese el peso (entre 10kg y 100kg) \n ")
    peso = float(peso)

    while(peso < 10 or peso > 100):
            peso = input("ERROR, Ingrese un peso valido (entre 10kg y 100kg) \n ")
            peso = float(peso)

    precio = input("Ingrese el precio por kilo \n ")
    precio = float(precio)

    while(precio < 0):
        precio = input("ERROR, Ingrese un precio valido \n ")
        precio = float(precio)

    tipo = input('Ingrese el tipo de producto ("v", "a", "m");(vegetal, animal, mezcla)')
    
    while (tipo != "a" and tipo != "v" and tipo != "m" ):
        tipo = input('ERROR, Ingrese el tipo de producto ("v", "a", "m");(vegetal, animal, mezcla)')






