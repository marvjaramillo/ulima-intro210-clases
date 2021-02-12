def imprimir(coleccion):
    for i in range(len(coleccion)):
        print(coleccion[i])

if __name__ == "__main__":
    lista = [1, 2, 3, 4]
    tupla = (5, 6, 7, 8)
    imprimir(lista)
    imprimir(tupla)