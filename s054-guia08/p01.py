def convertir_lista(lista):
    #Definimos un diccionario en blanco
    diccionario = {}
    #Recorremos la lista
    for i in range(len(lista)):
        #Cada elemento de la lista es una tupla
        tupla = lista[i]

        #El primer elemento de la tupla debe ser la clave
        clave = tupla[0]
        #El segundo elemento de la tupla debe ser el valor
        valor = tupla[1]
        #Agregamos el elemento al diccionario
        diccionario[clave] = valor
    return diccionario

if __name__ == "__main__":
    lista_puntos = [(1, 1), (2, 2), (3, 5)]
    diccionario = convertir_lista(lista_puntos)
    print(diccionario)
    