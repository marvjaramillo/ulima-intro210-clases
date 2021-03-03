def contar_palabras(nombre_archivo, palabra):
    cantidad = 0
    archivo = open(nombre_archivo, encoding="utf-8")
    
    for linea in archivo:
        lista_palabras = linea.split()        
        for palabra in lista_palabras:
            print(palabra)
            if(palabra.upper() == palabra):
                cantidad = cantidad + 1

    return cantidad

if __name__ == "__main__":
    cantidad = contar_palabras("data/texto.txt", "UNA")
    print("Cantidad de apariciones:", cantidad)
