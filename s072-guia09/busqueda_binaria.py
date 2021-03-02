import random

def busqueda_binaria(lista, valor):
    indice = -1
    #Cuando el algoritmo inicia, analizamos la lista completa
    izquierda = 0
    derecha = len(lista) - 1
    #Condiciones del bucle:
    #1) Mientras haya elementos que buscar (izquierda <= derecha)
    #2) Mientras no se haya encontrado el elemento (indice == -1)
    while(izquierda <= derecha and indice == -1):
        #Obtenemos el indice del elemento central        
        medio = (izquierda + derecha) // 2
        if(valor < lista[medio]):
            #Buscamos a la izquierda
            #Limite derecho debe estar a la izquierda del elemento central
            derecha = medio - 1
        elif(valor > lista[medio]):
            #Buscamos a la derecha
            #Limite izquierdo debe estar a la derecha del elemento central
            izquierda = medio + 1
        else:
            indice = medio
    return indice


if __name__ == "__main__":
    lista = [3, 4, 11, 22, 45, 64, 123, 200, 324]
    print(lista)
    valor = 45
    indice = busqueda_binaria(lista, valor)
    print("Respuesta: ", indice)
    

    #[2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 7, 8, 12]