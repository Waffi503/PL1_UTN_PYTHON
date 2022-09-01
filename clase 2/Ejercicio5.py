from array import array


habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    }
]
industrias_wayne = {}
array  = []

for habilidad in habilidades:
    tupla = (habilidad['Nombre'],habilidad['Poder'])
    array.append(tupla)

array.sort(key = lambda x: x[1])
industrias_wayne['habilidades_UTN'] = array


for categoria in industrias_wayne:
    index =  1
    print("{}:".format(categoria))
    for habilidad in industrias_wayne[categoria]:
        print("Habilidad {}: {} | {} ".format(index, habilidad[0], habilidad[1] ))
        index += 1
