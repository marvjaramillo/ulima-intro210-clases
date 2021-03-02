import random
from ordenamiento import burbuja
from funciones import generar_lista

def es_primo(n):
    cont = 0
    for i in range(1, n + 1):
        if(n % i == 0):
            cont = cont + 1
    if(cont == 2):
        return True
    else:
        return False

if __name__ == "__main__":
    lista = generar_lista(100, 2, 300)
    print("Lista original: ", lista)
    burbuja(lista)
    print("Lista ordenada: ", lista)
    
    lista_primos = []
    for i in range(len(lista)):
        elemento = lista[i]
        if(es_primo(elemento) == True):
            lista_primos.append(elemento)
    
    print("Lista de primos: ", lista_primos)
    print("Cantidad de elementos en lista original: ", len(lista))
    print("Cantidad de elementos en lista de primos: ", len(lista_primos))
