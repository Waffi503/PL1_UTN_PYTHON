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


print("Bievenido al programa")
pagar_bruto_total = 0
total_kilos = 0
i = 1
while (continuar != "no"):

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

    tipo = input('Ingrese el tipo de producto ("v", "a", "m");(vegetal, animal, mezcla) \n')
    
    while (tipo != "a" and tipo != "v" and tipo != "m" ):
        tipo = input('ERROR, Ingrese el tipo de producto ("v", "a", "m");(vegetal, animal, mezcla) \n')

    if (i == 1 or precio > precio_mas_alto):
        precio_mas_alto = precio
        precio_mas_alto_tipo = tipo
    
    total_kilos += peso
    pagar_bruto_total += precio * peso
    i += 1
    continuar = input('Quiere continuar ? Ingres "no" para salir del programa \n')

print('\n')
print('\n')
print('\n')
print('\n')
print('El importe total bruto es: ' + str(pagar_bruto_total) + '$')

if total_kilos > 300:
    pagar_descuento = pagar_bruto_total * 0.75
    print('El precio a pagar con descuento es: ' + str(pagar_descuento) + '$')
elif total_kilos > 100:
    pagar_descuento = pagar_bruto_total * 0.85
    print('El precio a pagar con descuento es: ' + str(pagar_descuento) + '$')
else:
    print('No hay descuento :(')


if precio_mas_alto_tipo == "a":
    print('El tipo mas caro es  Animal')
elif precio_mas_alto_tipo == "m":
    print('El tipo mas caro es Mezcla')
else:
    print('El tipo mas caro es vegetal')

promedio_kilo = pagar_bruto_total / total_kilos

print('El promedio por kilo es: ' +str(promedio_kilo) + '$')

    
    






