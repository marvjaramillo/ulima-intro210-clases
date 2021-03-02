import ordenamiento as ord
from funciones import generar_lista


if __name__ == "__main__":    
    lista = generar_lista(100, 0, 9)
    lista2 = []
    ord.burbuja(lista)
    print(lista)
    for i in range(50):
        lista2.append(lista[i])
    
    print(lista2)

