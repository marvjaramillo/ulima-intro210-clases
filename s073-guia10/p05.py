import ordenamiento as ord
import random
import funciones as f

if __name__ == "__main__":
    lista = f.generar_lista(50, 1, 50)    
    print("Lista: ", lista)
    print("Lista ordenada: ", ord.quicksort(lista))