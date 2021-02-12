def buscar(lista, valor):
    indice = -1
    for i in range(len(lista)):
        if(lista[i] == valor):
            indice = i
            break
    return indice

def eliminar_duplicados(lista):
    #Iniciamos lista de respuesta en blanco
    res = []
    #Recorremos la lista de entrada
    for i in range(len(lista)):
        #Por cada elemento de la lista
        elemento = lista[i]
        #Buscamos el elemento en la lista de respuesta
        if(buscar(res, elemento) == -1):
            #Si el elemento no se encuentra, lo agrego
            res.append(elemento)
    return res

if __name__ == "__main__":
    lista = [1, 23, 23, 4, 3, 1, 1, 4, 8, 13]
    nueva_lista = eliminar_duplicados(lista)
    print(lista)
    print(nueva_lista)