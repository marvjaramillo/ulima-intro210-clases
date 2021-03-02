def burbuja(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if(lista[j] > lista[j + 1]):
                #lista[j], lista[j + 1] = lista[j + 1], lista[j]
                aux = lista[j + 1]
                lista[j + 1] = lista[j] 
                lista[j] = aux
                

if __name__ == "__main__":
    lista = [1, 34, 4, 355, 23, 4556, 25, 39]
    burbuja(lista)
    print(lista)
