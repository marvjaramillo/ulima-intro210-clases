import busqueda_binaria as bb
def generar_lista(inicio, fin, incremento):
    lista = []
    for i in range(inicio, fin + 1, incremento):
        cuadrado = i ** 2
        lista.append(cuadrado)
    return lista

if __name__ == "__main__":
    inicio = 10
    fin = 20
    incremento = 2
    lista = generar_lista(inicio, fin, incremento)
    for i in range((inicio ** 2) + (3 - (inicio ** 2) % 3), (fin + 1) ** 2, 3):
        indice = bb.busqueda_binaria(lista, i)
        if(indice != -1):
            print("Valor", i, "encontrado en posicion", indice)

    print(lista)
    #14