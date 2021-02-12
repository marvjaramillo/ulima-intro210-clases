def buscar_asistente(lista_asistentes, nombre_buscar):
    encontrado = False
    #Recorrer la lista de asistentes
    for i in range(len(lista_asistentes)):
        #Verificamos si el elemento es igual al nombre que se esta buscando
        if(lista_asistentes[i].upper() == nombre_buscar.upper()):
            encontrado = True
    if(encontrado == True):
        print("La persona estuvo presente")
    else:
        print("La persona no estuvo presente")

def main():
    nombre = "chang"
    asistentes = ["PEREZ", "CHANG", "GONZALES", "BARCO"]
    buscar_asistente(asistentes, nombre)
    
if __name__ == "__main__":
    main()