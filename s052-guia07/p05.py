def eliminar_duplicados(lista):
    i = 0
    #Por cada elemento de la lista
    while(i < len(lista)):
        encontrado = False
        #Busco el elemento hacia la izquierda
        for j in range(i):
            #Si elemento aparece a la izquierda
            if(lista[j] == lista[i]):
                encontrado = True
                break
        if(encontrado):
            #Si el elemento aparece a la izquierda lo eliminamos
            lista.pop(i)
        else:
            #Si el elemento no aparece, buscamos el siguiente
            i = i + 1

if __name__ == "__main__":
    lista = [1, 2, 1, 1, 2, 3, 4, 9, 9]
    print(lista)
    eliminar_duplicados(lista)
    print(lista)
