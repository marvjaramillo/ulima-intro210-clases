import random
def generar_lista(cantidad, inicio, fin):
    lista = []
    for i in range(cantidad):
        valor = random.randint(inicio, fin)
        lista.append(valor)
    return lista

def obtener_pares(lista):
    res = []
    for i in range(len(lista)):
        if(lista[i] % 2 == 0):
            res.append(lista[i])
    return res

if __name__ == "__main__":
    lista = generar_lista(100, 0, 9)
    lista_pares = obtener_pares(lista)
    print(lista)
    print(lista_pares)