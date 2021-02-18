TARIFA_KM = 2.5

def cotizar():
    continuar = True
    while(continuar == True):
        cant_paquetes = int(input("Ingrese cantidad de paquetes: "))
        kilometros = float(input("Ingrese cantidad de Kilometros: "))
        precio = cant_paquetes * kilometros * TARIFA_KM
        if(precio > 100):
            precio = 0.9 * precio
        print("El precio del servicio es:", precio)

        opcion = input("Presione 'S' para realizar otra cotizacion: ")
        if(opcion.upper() != "S"):
            continuar = False