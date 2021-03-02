def busqueda_secuencial(lista, valor):
    indice = -1
    for i in range(len(lista)):
        if(lista[i] == valor):
            indice = i
            #break
    return indice

def encontrar_apariciones(lista, valor):
    indices = []
    for i in range(len(lista)):
        if(lista[i] == valor):
            indices.append(i)
    return indices

if __name__ == "__main__":
    lista = [123, 324, 3, 4, 45, 22, 11, 64, 200]
    lista2 = [29, 399, 210, 14, 210, 222, 210]
    valor = 210
    indice = busqueda_secuencial(lista, valor)
    print(indice)
    lista_indices = encontrar_apariciones(lista2, valor)
    print(lista_indices)

