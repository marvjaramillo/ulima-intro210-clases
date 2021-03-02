import ordenamiento as ord
def leer_pesos():
    continuar = True
    lista = []
    suma = 0
    while(continuar == True):
        peso = int(input("Ingrese peso: "))
        if(peso <= 0):
            continuar = False
        else:
            lista.append(peso)
            suma = suma + peso
    lista.append(suma // len(lista))
    return lista

if __name__ == "__main__":
    lista = leer_pesos()
    lista_ordenada = ord.quicksort(lista)
    print("Lista original: ", lista)
    print("Lista ordenada: ", lista_ordenada)
