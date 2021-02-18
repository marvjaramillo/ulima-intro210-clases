OPCION_COTIZAR = 1
OPCION_PARTICIPAR = 2
OPCION_DETENER = 3
OPCION_CREDITOS = 4

lista_opciones = [  "Cotizar envio",
                    "Participar por un premio",
                    "Detener aplicacion",
                    "Creditos"
                 ]

def mostrar_menu():
    print("*" * 20)
    print("*" * 20)
    for i in range(len(lista_opciones)):
        print((i + 1), ". ", lista_opciones[i])
    print("*" * 20)

def obtener_opcion():
    opcion = int(input("Seleccione una opcion: "))
    return opcion
