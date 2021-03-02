def burbuja(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if(lista[j] > lista[j + 1]):
                #lista[j], lista[j + 1] = lista[j + 1], lista[j]
                aux = lista[j + 1]
                lista[j + 1] = lista[j] 
                lista[j] = aux

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

