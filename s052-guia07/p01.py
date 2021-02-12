def obtener_lista_acumulada(lista):
    suma = 0
    #Definimos una lista en blanco
    respuesta = []
    for i in range(len(lista)):
        #Sumar los elementos de la lista leidos hasta el momento
        suma = suma + lista[i]
        #Agregamos el valor a la lista de respuesta
        respuesta.append(suma)
    return respuesta

def main():
    lista = obtener_lista_acumulada([10, 15, 8, 7, 14])
    print(lista)
    
if __name__ == "__main__":
    main()