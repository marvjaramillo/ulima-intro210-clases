def leer(nombre_archivo, cant_lineas):
    MAX_LINEAS = 11
    if(cant_lineas > MAX_LINEAS):
        cant_lineas = MAX_LINEAS
    #Abrir el archivo
    archivo = open(nombre_archivo)
    contador = 0
    
    #Recorrer linea por linea
    for linea in archivo:
        print(linea, end="")
        contador = contador + 1

        if(contador == cant_lineas):
            break
    #Cerrar el archivo
    archivo.close()

if __name__ == "__main__":
    leer("data/archivo1.txt", 8)