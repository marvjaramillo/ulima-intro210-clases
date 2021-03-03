def tiene_orden_ascendente(lista):
    res = True
    for i in range(len(lista) - 1):
        if(lista[i] >= lista[i + 1]):
            res = False
            break
    return res

if __name__ == "__main__":
    lista = [2, 6, 18, 54]
    print(lista)
    ascendente = tiene_orden_ascendente(lista)
    print(ascendente)