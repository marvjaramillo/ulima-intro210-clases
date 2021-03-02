import busqueda_binaria as bb
def leer_datos(valor_escape):
    lista = []
    continuar = True
    suma = 0
    while(continuar):
        valor = int(input("Ingrese valor o cero para terminar: "))
        if(valor != valor_escape):
            lista.append(valor)
            suma = suma + valor
        else:
            continuar = False
    
    promedio = suma // len(lista)
    lista.append(promedio)

    return lista

if __name__ == "__main__":
    lista = leer_datos(0)
    lista.sort()
    print(lista)
    indice = bb.busqueda_binaria(lista, 50)
    if(indice == -1):
        print("Valor no esta en la lista")
    else:
        print("Valor encontrado en el indice", indice)

