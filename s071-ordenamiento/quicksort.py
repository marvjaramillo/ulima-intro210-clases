def quicksort(lista):
    if(len(lista) <= 1):
        return lista
    else:
        pivot = lista[0]
        menores = []
        mayores = []
        for i in range(1, len(lista)):
            if(lista[i] > pivot):
                mayores.append(lista[i])
            else:
                menores.append(lista[i])
        mayores = quicksort(mayores)
        menores = quicksort(menores)
        return menores + [pivot] + mayores

if __name__ == "__main__":
    lista = [1, 34, 4, 355, 23, 4556, 25, 39]
    lista_ordenada = quicksort(lista)
    print(lista_ordenada)